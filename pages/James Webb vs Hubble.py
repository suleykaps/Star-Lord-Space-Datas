import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2


st.set_page_config("James Webb ve Hubble Uzay Telekobu", "🔭")


st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/telescope_1f52d.png",
    width=120,
)

st.header("James Webb ve Hubble Uzay Telekobu")

st.write("Bu sayfa da James Webb ve Hubble Uzay Teleskobundan çekilen görüntüleri karşılaştırarak göreceksiniz. "
         "Bu projenin yapımcısı John Christensen'a teşekkür ederiz.")
st.markdown("**Twitter**    >   https://twitter.com/JohnnyC1423")


st.markdown("### Southern Nebula - NGC 3132")
st.markdown("NGC 3132 - Patlak Sekiz Bulutsusu veya Güneyin Halka Bulutsusu- Yelken takımyıldızı yönünde bulunan parlak bir gezegenimsi bulutsu. "
            "Gaz kabuğu 24 km−1 hızla genişlemektedir. Dünya'dan yaklaşık uzaklığı 2000 ışık yılıdır.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Hubble Uzay Teleskobu",
    label2="James Webb Uzay Teleskobu",
)


st.markdown("### Galaxy Cluster - SMACS 0723")
st.markdown("SMACS J0723.3-7327 (SMACS 0723), Uçanbalık takımyıldızı'nda yer alan ve comoving mesafesi "
            "yaklaşık olarak 5,12 milyar ışık yılı olan bir gökada kümesidir.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
    img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
    label1="Hubble Uzay Teleskobu",
    label2="James Webb Uzay Teleskobu",
)

st.markdown("### Carina Nebula - NGC 3372")
st.markdown("Eta Karina Bulutsusu, gökadanın Yay Kolu'nda, bizden 9000 ışıkyılı uzaklıkta dev bir bulutsudur. "
            "Bu çok büyük bir uzaklık olmasına rağmen, bulutsu çıplak gözle görülebilecek kadar parlaktır.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/carina_2800.png",
    img2="https://www.webbcompare.com/img/webb/carina_2800.jpg",
    label1="Hubble Uzay Teleskobu",
    label2="James Webb Uzay Teleskobu",
)

st.markdown("### Stephan's Quintet - NGC 7318B")
st.markdown("NGC 7318B, Kanatlıat takımyıldızı bölgesinde yaklaşık olarak 300 milyon ışık yılı uzaklıkta "
            "bulunan ve Stephan Beşlisi içerisinde NGC 7318A ile çarpışma sürecindeki çubuklu sarmal gökada. "
            "Édouard Jean-Marie Stephan tarafından 23 Eylül 1876 yılında keşfedilmiştir.")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/stephans_quintet_2800.jpg",
    img2="https://www.webbcompare.com/img/webb/stephans_quintet_2800.jpg",
    label1="Hubble Uzay Teleskobu",
    label2="James Webb Uzay Teleskobu",
)