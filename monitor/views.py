from django.http import HttpResponse
from django.views import generic
from .models import Location, WeatherData
from django.contrib.auth.mixins import LoginRequiredMixin
import io
import matplotlib.pyplot as plt
import logging
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
import os
from monitor import addCsv


logger = logging.getLogger('development')


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Location
    paginate_by = 5
    ordering = ['-updated_at']
    template_name = 'monitor/index.html'


class DetailView(generic.DetailView):
    model = Location
    template_name = 'monitor/detail.html'


def my_test_500_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponseServerError


# グラフ作成
def setPlt(pk):
    # 折れ線グラフを出力

    weather_data = WeatherData.objects.select_related('location').filter(location_id=pk)  # 対象ロケーションの気象データを取得
    # weather_data = WeatherData.objects.raw('SELECT * FROM weather_data WHERE location_id = %s', str(pk)) # このクエリでもOK
#    x = [data.data_datetime for data in weather_data] # 日時
    x = [data.nengetu for data in weather_data] # 日時
    y1 = [data.kuchou for data in weather_data] # 空調
    y2 = [data.dentou for data in weather_data]  # 電灯
    y3 = [data.goukei for data in weather_data]  # 合計

#グラフサイズ・X軸表示編集
    plt.figure(figsize=(20, 10)) # figureの縦横の大きさ
    plt.xticks(rotation=90)


    plt.title("電力使用量推移", fontname="MS Gothic")
    plt.xlabel("年月", fontname="MS Gothic")
    plt.ylabel("電力使用量", fontname="MS Gothic")
    plt.plot(x, y1, marker="o")
    plt.plot(x, y2, marker="o")
    plt.plot(x, y3, marker="o")
    plt.legend()

    plt.legend([u'空調', u'電灯',u'合計'], prop={"family":"MS Gothic"})

#    plt.title("電力使用量")
#    plt.scatter(x0, y0, label="label-A")
#    plt.scatter(x1, y1, label="label-B")
#    plt.xlabel("年月")
#    plt.xlabel("Y-LABEL")
#    plt.legend()
#    plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=30)



# svgへの変換
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s
def get_svg(request, pk):
    setPlt(pk)  # create the plot
    svg = pltToSvg()  # convert plot to SVG
    plt.cla()  # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response



# アップロードされたファイルのハンドル


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'monitor/post_list.html', {'posts': posts})
