from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers.votes import vote
from . import models
from .database import engine
from .routers import post, user, auth, votes
from .config import settings
from app import database
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


print(settings.database_password)

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()


origins = ['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):

    return templates.TemplateResponse('index.html', {'request': request})


@app.get("/about_us", response_class=HTMLResponse)
def get_about(request: Request):

    return templates.TemplateResponse('about-us.html', {'request': request})


@app.get("/lichnyy-opyt/", response_class=HTMLResponse)
def get_lichnyy_opyt(request: Request):

    return templates.TemplateResponse('lichnyy-opyt.html', {'request': request})


@app.get("/magazine_sites", response_class=HTMLResponse)
def get_postblog(request: Request):

    return templates.TemplateResponse('post.html', {'request': request})


@app.get("/design", response_class=HTMLResponse)
def get_design(request: Request):

    return templates.TemplateResponse('design.html', {'request': request})


@app.get("/contact", response_class=HTMLResponse)
def get_contact(request: Request):

    return templates.TemplateResponse('contact.html', {'request': request})


@app.get("/base_header", response_class=HTMLResponse)
def get_header(request: Request):

    return templates.TemplateResponse('base_header.html', {'request': request})


@app.get("/base_footer", response_class=HTMLResponse)
def get_footer(request: Request):

    return templates.TemplateResponse('base_footer.html', {'request': request})


@app.get("/opencv-s-python-rassmotrim-izobrazheniya-meksikan/", response_class=HTMLResponse)
def get_opencv(request: Request):

    return templates.TemplateResponse('opencv-s-python-rassmotrim-izobrazheniya-meksikan.html', {'request': request})


@app.get("/typography", response_class=HTMLResponse)
def get_typography(request: Request):

    return templates.TemplateResponse('typography.html', {'request': request})


@app.get("/razrabotka-doski-obyavleniy-na-shablone-bitriks/", response_class=HTMLResponse)
def get_razrabotka_doski(request: Request):

    return templates.TemplateResponse('razrabotka-doski-obyavleniy-na-shablone-bitriks.html', {'request': request})


@app.get("/4-sposoba-zaporot-ai-ti-proect-i-poluchit-ban-ot-mail-ru/", response_class=HTMLResponse)
def get_4_sposoba_zaporot(request: Request):

    return templates.TemplateResponse('4-sposoba-zaporot-ai-ti-proect-i-poluchit-ban-ot-mail-ru.html', {'request': request})


@app.get("/vybor-sfery-deyatelnosti/", response_class=HTMLResponse)
def get_vybor_sfery(request: Request):

    return templates.TemplateResponse('vybor-sfery-deyatelnosti.html', {'request': request})


@app.get("/registraciya-firmy-v-nalogovoy-inspek/", response_class=HTMLResponse)
def get_registraciya_firmy(request: Request):

    return templates.TemplateResponse('registraciya-firmy-v-nalogovoy-inspek.html', {'request': request})


@app.get("/pochemu-zakryvayutsya-startapy/", response_class=HTMLResponse)
def get_pochemu_zakryvayutsya(request: Request):

    return templates.TemplateResponse('pochemu-zakryvayutsya-startapy.html', {'request': request})


@app.get("/perviy-ay-ti-proekt-vhodim-v-temu-obschiy-kontekst/", response_class=HTMLResponse)
def get_perviy_ay_ti(request: Request):

    return templates.TemplateResponse('perviy-ay-ti-proekt-vhodim-v-temu-obschiy-kontekst.html', {'request': request})


@app.get("/theme-post", response_class=HTMLResponse)
def get_theme_post(request: Request):

    return templates.TemplateResponse('theme-post.html', {'request': request})


@app.get("/slider", response_class=HTMLResponse)
def get_slider(request: Request):

    return templates.TemplateResponse('slider.html', {'request': request})


@app.get("/python_razrabotka/", response_class=HTMLResponse)
def get_python_razrabotka(request: Request):

    return templates.TemplateResponse('python_razrabotka.html', {'request': request})


@app.get("/drevnie-tekhnologii/", response_class=HTMLResponse)
def get_drevnie_tekhnologii(request: Request):

    return templates.TemplateResponse('drevnie-tekhnologii.html', {'request': request})


@app.get("/krizis-crisis/", response_class=HTMLResponse)
def get_krizis_crisis(request: Request):

    return templates.TemplateResponse('krizis-crisis.html', {'request': request})


@app.get("/base_right_body/", response_class=HTMLResponse)
def get_base_right_body(request: Request):

    return templates.TemplateResponse('base_right_body.html', {'request': request})


@app.get("/news/", response_class=HTMLResponse)
def get_news(request: Request):

    return templates.TemplateResponse('news.html', {'request': request})


@app.get("/chto-ne-skazala-greta-tunberg/", response_class=HTMLResponse)
def get_chto_ne_skazala_greta_tunberg(request: Request):

    return templates.TemplateResponse('chto-ne-skazala-greta-tunberg.html', {'request': request})


@app.get("/budushhee-v-nashikh-rukakh-davos-2021/", response_class=HTMLResponse)
def get_budushhee_v_nashikh(request: Request):

    return templates.TemplateResponse('budushhee-v-nashikh-rukakh-davos-2021.html', {'request': request})


@app.get("/vremya-vpered/", response_class=HTMLResponse)
def get_vremya_vpered(request: Request):

    return templates.TemplateResponse('vremya-vpered.html', {'request': request})


@app.get("/artefakty-drevnej-ameriki-kotorye-otsu/", response_class=HTMLResponse)
def get_artefacty_drevnej_am(request: Request):

    return templates.TemplateResponse('artefakty-drevnej-ameriki-kotorye-otsu.html', {'request': request})


@app.get("/artefakty-drevnej-ameriki-podkhod-rasshifrovat-meksikanskie-piktogrammy/", response_class=HTMLResponse)
def get_artefacty_drevnej_am_podhod_rasch(request: Request):

    return templates.TemplateResponse('artefakty-drevnej-ameriki-podkhod-rasshifrovat-meksikanskie-piktogrammy.html', {'request': request})


@app.get("/pagination/", response_class=HTMLResponse)
def get_artefacty_drevnej_am_podhod_rasch(request: Request):

    return templates.TemplateResponse('pagination.html', {'request': request})


@app.get("/share/", response_class=HTMLResponse)
def get_artefacty_drevnej_am_podhod_rasch(request: Request):

    return templates.TemplateResponse('share.html', {'request': request})
