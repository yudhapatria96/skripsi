from django.shortcuts import render, redirect
from input_data.models import PenjualanModel
from .models import ForecastingPenjualanModel
from . import forms
# Create your views here.
# from . import forms
# from . import models
def index(request):
    post = PenjualanModel.objects.all()
    # contact_form = forms.ContactForm()
    # for postss in post:
    #     print(postss)
    dating_form = forms.DatingForm()
    thismonth= {
        '1' : "januari",
        '2' : "februari",
        '3' : "maret",
        '4' : "april",
        '5' : "mei",
        '6' : "juni",
        '7' : "juli",
        '8' : "agustus",
        '9' : "september",
        '10' : "oktober",
        '11' : "november",
        '12' : "desember"
    }
    # years= PenjualanModel.objects.all().order_by('tahun_transaksi')
    # len_year = len(years)
    # print(years[len_year - 1].tahun_transaksi)
        
    context = {
        'heading':'Forecasting',
        'dating_form': dating_form,
        # 'data_form':contact_form,
        # 'posts' : post,

    }
    jumlah_hotel = []
    jumlah_mall = []
    jumlah_apartemen = []
    jumlah_c441 = []
    jumlah_c442 = []
    jumlah_c443 = []
    jumlah_c451 = []
    jumlah_c452 = []
    jumlah_c453 = []
    jumlah_c461 = []
    jumlah_c462 = []
    jumlah_c463 = []
    jasa_pembersih_air = []
    jasa_pembersih_kerak_sillica = []
    jasa_pembersih_cooling_tower = []
    jasa_pembersih_stp = []
    jumlah_asam_sulfat = []
    jumlah_molases = []
    jumlah_hcl = []
    jumlah_abf = []
    bulan_tertentu = []
    semua = []
    x = 0
    x_kuadrat = 0
    total_x = 0
    b = 0 
    a = 0
    n = 0
    jumlah_bulan = 0
    rata_rata_penjualan_bulan_tertentu = 0 
    jumlah_penjualan_bulan_tertentu = 0
    rata_rata_penjualan_total = 0
    index_musiman = 0
    years= PenjualanModel.objects.all().order_by('tahun_transaksi')
    year_int = years[len(years) - 1].tahun_transaksi
    index_tahun = 0
    if request.method == 'POST':
        bulan = request.POST['bulan_dan_tahun_prediksi_month'] 
        tahun = request.POST['bulan_dan_tahun_prediksi_year']   
        print(bulan)
        print(tahun)
        if(bulan != '0' and tahun != '0'):
            index_tahun = ((int(tahun) - year_int - 1) * 12)
            si_x = index_tahun + (int(request.POST['bulan_dan_tahun_prediksi_month'] ))
            
            # print(thismonth[bulan])
            for posts in post:
                # print(posts.jumlah_hotel)
                # print(posts.jumlah_C441)
                x += 1
                x_kuadrat = x_kuadrat + (x * x)
                total_x = total_x + x
                jumlah_hotel.append(posts.jumlah_hotel)
                jumlah_mall.append(posts.jumlah_mall)
                jumlah_apartemen.append(posts.jumlah_apartemen)
                jumlah_c441.append(posts.jumlah_C441)
                jumlah_c442.append(posts.jumlah_C442)
                jumlah_c443.append(posts.jumlah_C443)
                jumlah_c451.append(posts.jumlah_C451)
                jumlah_c452.append(posts.jumlah_C452)
                jumlah_c453.append(posts.jumlah_C453)
                jumlah_c461.append(posts.jumlah_C461)
                jumlah_c462.append(posts.jumlah_C462)
                jumlah_c463.append(posts.jumlah_C463)
                jasa_pembersih_air.append(posts.jasa_pembersih_air)
                jasa_pembersih_kerak_sillica.append(posts.jasa_pembersih_kerak_sillica)  
                jasa_pembersih_cooling_tower.append(posts.jasa_pembersih_cooling_tower)
                jasa_pembersih_stp.append(posts.jasa_pembersih_stp)
                jumlah_asam_sulfat.append(posts.jumlah_asam_sulfat)
                jumlah_molases.append(posts.jumlah_molases)
                jumlah_hcl.append(posts.jumlah_hcl)
                jumlah_abf.append(posts.jumlah_abf)
                bulan_tertentu.append(posts.bulan_transaksi)
                # if(thismonth[bulan] == posts.bulan_transaksi):
                #     jumlah_bulan += 1       
            n = x
            # print(jasa_pembersih_air)
            # print(x_kuadrat)
            # print(total_x)
            # print(x)
                
            semua = [jumlah_hotel, jumlah_mall,jumlah_apartemen,jumlah_c441,jumlah_c442,
            jumlah_c443,jumlah_c451,jumlah_c452,jumlah_c453,jumlah_c461,jumlah_c462,jumlah_c463,
            jasa_pembersih_air,
            jasa_pembersih_kerak_sillica,
            jasa_pembersih_cooling_tower,
            jasa_pembersih_stp,
            jumlah_asam_sulfat,
            jumlah_molases,
            jumlah_hcl,
            jumlah_abf]
            hitung = 0
            for satuan in semua:
                hitung+= 1
                x_y = 0
                xy = 0
                total_xy = 0
                total_y = 0
                b = 0
                a = 0
                y = 0
                for satudata in satuan :
                    if(thismonth[bulan] == bulan_tertentu[x_y]):
                       jumlah_bulan += 1 
                       jumlah_penjualan_bulan_tertentu += satudata
                    x_y += 1
                    xy = x_y * satudata
                    total_xy = total_xy + xy
                    total_y = total_y + satudata
                 
                b = ((n * total_xy)-(total_x * total_y)) / ((n * x_kuadrat) - (total_x * total_x))
                a = (total_y - (b * total_x))/n
                y = a + (b * (si_x + x_y))   
                       
                rata_rata_penjualan_bulan_tertentu = jumlah_penjualan_bulan_tertentu / jumlah_bulan
                rata_rata_penjualan_total = total_y / x_y
                
                index_musiman = rata_rata_penjualan_bulan_tertentu / rata_rata_penjualan_total
                y_index_musiman = y * index_musiman
                print(y_index_musiman)
                
                
    return render(request, 'forecasting/index.html',context)