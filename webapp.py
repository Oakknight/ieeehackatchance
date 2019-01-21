from flask import Flask, jsonify, redirect, url_for, escape, request, render_template
import requests
import devamidb


def olurmu(sinirlama):
    if len(sinirlama):
        return False
    return True

def hasta_isim_al(tckn):
    hasta_id=devamidb.TCdenID(tckn)
    hasta_bilgi=devamidb.hastaBilgi(hasta_id)
    return hasta_bilgi[0]

app = Flask(__name__,static_url_path='/static')

@app.route('/', methods=['GET','POST'])
def main():
    if request.method=="POST":
        ilac=request.form["ilac"]
        tckn=request.form["tckn"]
        return redirect("/sorgu/{0}/{1}".format(tckn,ilac))
    return render_template("girdi.html",home=url_for('main'))

@app.route('/sorgu/<tckn>/<ilac>',methods=["GET"])
def result(tckn,ilac):
    sinirlama=devamidb.ilacKontrol(tckn,ilac)
    risksiz=olurmu(sinirlama)
    if risksiz:
        return render_template("sonuciyi.html",hasta_isim=hasta_isim_al(tckn),ilac_isim=ilac)
    else:
        return render_template("sonuckotu.html",sinirlama=sinirlama,hasta_isim=hasta_isim_al(tckn),ilac_isim=ilac)

@app.route('/ilac/<ilac>',methods=['GET'])
def ilac_goster(ilac):
    return render_template("ilac.html",ilac=ilac)

@app.route('/hasta/<hasta>',methods=['GET'])
def hasta_goster(hasta):
    return render_template("hasta.html",hasta=hasta)

if __name__ == '__main__':
    app.run(debug=True)
