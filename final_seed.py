import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "corporate_hindi.settings")
django.setup()

from dash.models import Category, Author, team
from django.utils.text import slugify

print("Seeding Categories...")
wanted_categories = [
    {"title": 'कवर स्टोरी', "slug": 'cover-story', "display_order": 1},
    {"title": 'प्राइम पर्सनैलिटी', "slug": 'prime-personality', "display_order": 7},
    {"title": 'संपादकीय', "slug": 'सपदकय', "display_order": 16},
    {"title": 'स्टेट इनसाइट', "slug": 'सटट-इनसइट', "display_order": 17},
    {"title": 'कारपोरेट न्यूज़', "slug": 'करपरट-नयज', "display_order": 18},
    {"title": 'सीएसआर फोकस', "slug": 'सएसआर-फकस', "display_order": 19},
    {"title": 'इन दिनों', "slug": 'इन-दन', "display_order": 20},
    {"title": 'जीवनमंथन', "slug": 'जवनमथन', "display_order": 21},
    {"title": 'दो बातें', "slug": 'द-बत', "display_order": 22},
    {"title": 'इनसाइट स्टोरी', "slug": 'इनसइट-सटर', "display_order": 23},
    {"title": 'सिने इनसाइट', "slug": 'सन-इनसइट', "display_order": 24},
    {"title": 'हेल्थ एन्ड वैलनेस', "slug": 'हलथ-एनड-वलनस', "display_order": 25},
]

for idx, cat_data in enumerate(wanted_categories):
    title = cat_data["title"]
    c, created = Category.objects.get_or_create(
        title=title,
        defaults={
            'slug': cat_data["slug"] or slugify(title, allow_unicode=True),
            'meta_title': title,
            'meta_description': title,
            'meta_keywords': title,
            'description': title,
            'status': 'Enabled',
            'display_order': cat_data["display_order"],
            'show_in_nav': True
        }
    )
    if not created:
        c.display_order = cat_data["display_order"]
        c.status = 'Enabled'
        c.show_in_nav = True
        c.save()
    print(f"Category {title}: {'Created' if created else 'Updated'}")

# Disable categories that are not in wanted list
Category.objects.exclude(title__in=[c["title"] for c in wanted_categories]).update(status='Disabled', show_in_nav=False)

print("\nSeeding Authors...")
authors_data = [
    {"name": 'रश्मीत कौर चावला', "email": 'rashmeet@corporateimpact.com', "slug": 'rashmeet-kaur-chawla', "designation": 'संपादक', "description": 'रश्मीत एक रचनात्मक कंटेंट राइटर हैं जो सार्थक कहानी कहने के जुनून से प्रेरित हैं। वे स्पष्ट और आकर्षक कथाएं गढ़ती हैं जो एक स्थायी प्रभाव छोड़ती हैं। बिगस्टोरी नेटवर्क में एक संपादक के रूप में, वे ऐसी कहानियां साझा करने के लिए प्रतिबद्ध हैं जो बदलाव को प्रेरित करें, बातचीत को जन्म दें, और विविध समुदायों को जोड़ें, शब्दों की शक्ति का उपयोग करके समझ को बढ़ावा दें और एक अधिक समावेशी दुनिया का निर्माण करें।'},
    {"name": 'गुरबीर सिंह चावला', "email": 'connect@corporateimpact.in', "slug": 'gurbeer-singh-chawla', "designation": 'मीडिया उद्यमी और समूह संपादक', "description": 'गुरबीर सिंह चावला एक प्रतिष्ठित संपादक और डिजिटल मीडिया रणनीतिकार हैं, जिन्हें आधुनिक व्यवसाय, स्टार्टअप और प्रौद्योगिकी परिदृश्यों में उच्च प्रभाव वाली कहानियां गढ़ने का एक दशक से अधिक का अनुभव है। इकोसिस्टम विश्लेषण, उभरते बाज़ार रुझानों और एंटरप्राइज़-स्तरीय कहानी कहने में विशेषज्ञता रखते हुए, गुरबीर ने अग्रणी डिजिटल प्रकाशनों के लिए संपादकीय दिशा का सफलतापूर्वक नेतृत्व किया है, जिससे व्यापक दर्शक जुड़ाव और उद्योग में निर्णायक प्रतिष्ठा दोनों हासिल हुई है। एक विश्लेषणात्मक फिर भी गहराई से सुलभ लेखन शैली के लिए पहचाने जाने वाले, वे जटिल बाज़ार बदलावों और तकनीकी विकासों को सहजता से आकर्षक, कार्रवाई योग्य अंतर्दृष्टि में बदल देते हैं। ब्रांड की आवाज़ को ऊंचा उठाने और आधिकारिक कंटेंट हब तैयार करने के सिद्ध ट्रैक रिकॉर्ड के साथ, गुरबीर आज की तेज़ रफ़्तार डिजिटल अर्थव्यवस्था में आगे बढ़ने वाले पेशेवरों के लिए विश्वसनीय, भविष्योन्मुखी पत्रकारिता प्रदान करने के लिए समर्पित हैं।'},
    {"name": 'अंशिका भारद्वाज', "email": 'anshikabhardwaj1145@gmail.com', "slug": 'anshika-bhardwaj', "designation": 'कंटेंट डेवलपमेंट डायरेक्टर', "description": 'अंशिका भारद्वाज एक गतिशील कंटेंट रणनीतिकार और कहानीकार हैं, जो कंटेंट डेवलपमेंट डायरेक्टर के रूप में कार्यरत हैं, और प्रभावशाली, पाठक-केंद्रित कथाएं बनाने पर विशेष ध्यान देती हैं। मीडिया, संचार और डिजिटल प्रकाशन के प्रति जुनूनी, वे आकर्षक संपादकीय सामग्री, फीचर स्टोरीज़ और रचनात्मक अभियान विकसित करने में विशेषज्ञ हैं जो विचारों को पाठकों से सार्थक रूप से जोड़ते हैं। विवरण और उभरते रुझानों पर पैनी नज़र रखते हुए, वे अपने नेतृत्व वाली हर परियोजना में रचनात्मकता, स्पष्टता और दृष्टिकोण लाती हैं।'},
    {"name": 'प्रियंका चंदानी', "email": 'priyankaonreport@gmail.com', "slug": 'priyanka-chandani', "designation": 'एसोसिएट एडिटर', "description": 'प्रियंका चंदानी एक समर्पित कंटेंट रणनीतिकार और लेखिका हैं, जो जटिल विचारों को सम्मोहक मानवीय कहानियों में बदलने में माहिर हैं। एक संपादक के रूप में, वे ऐसी कहानियां उजागर करने के प्रति जुनूनी हैं जो नज़रिए को चुनौती दें और सार्थक संवाद को जन्म दें। विवरण पर पैनी नज़र और प्रामाणिक पत्रकारिता के प्रति समर्पण के साथ, प्रियंका मीडिया की शक्ति का उपयोग पुल बनाने, विविध आवाज़ों को बुलंद करने और गहराई से जुड़े समुदाय के निर्माण के लिए करती हैं।'},
    {"name": 'स्वेताक्षी लता', "email": 'swetakshilata2@gmail.com', "slug": 'swetakshi-lata', "designation": 'कंटेंट डेवलपमेंट एक्ज़ीक्यूटिव', "description": 'स्वेताक्षी लता एक रचनात्मक और विवरण-केंद्रित कंटेंट डेवलपमेंट एक्ज़ीक्यूटिव हैं, जिन्हें आकर्षक और सार्थक सामग्री तैयार करने का जुनून है। वे कंटेंट रिसर्च, संपादकीय समन्वय और डिजिटल तथा प्रिंट प्लेटफ़ॉर्म्स पर पाठक-अनुकूल कथाएं विकसित करने में विशेषज्ञ हैं। संचार रुझानों और दर्शक जुड़ाव की गहरी समझ के साथ, वे नए विचार और विचारशील कहानी कहने का योगदान देती हैं जो समग्र कंटेंट अनुभव को बेहतर बनाता है।'},
    {"name": 'प्राची गुप्ता', "email": 'prachig90@gmail.com', "slug": 'prachi-gupta', "designation": 'एसोसिएट एडिटर', "description": 'डॉ. प्राची गुप्ता 11 पुस्तकों की बेस्टसेलिंग लेखिका, टेड स्पीकर, और ईएनएन360 (एक अग्रणी शिक्षा उद्यम) तथा गैलियन पब्लिशिंग हाउस की गतिशील सीईओ हैं। यूनिवर्सिटी ऑफ लंदन से एमबीए और वास्तु शास्त्र में पीएचडी के साथ, वे प्राचीन ज्ञान को आधुनिक दृष्टिकोण के साथ जोड़ती हैं।\r\nवे रिसर्च फाउंडेशन ऑफ इंडिया की ब्रांड एंबेसडर और एक सेलिब्रिटी वास्तु विशेषज्ञ भी हैं। कई पुरस्कारों से सम्मानित इस कहानीकार की प्रशंसित लघु फिल्म ने 11 राष्ट्रीय और 2 अंतरराष्ट्रीय पुरस्कार जीते हैं, जो सिनेमा जगत में उनकी असाधारण प्रतिभा को दर्शाता है।\r\nअपने प्रभाव के लिए वैश्विक स्तर पर सम्मानित, डॉ. प्राची गुप्ता को 2025 में कर्मवीर चक्र पुरस्कार से नवाज़ा गया। वे भारत का वैश्विक प्रतिनिधित्व करते हुए कई राष्ट्रीय और अंतरराष्ट्रीय पत्रिकाओं के कवर पर छप चुकी हैं।\r\nदिल से एक जुनूनी शोधकर्ता, उन्होंने भारतीय वेदों में गहराई से अध्ययन किया है, और भगवद गीता, रामायण तथा महाभारत की कालजयी शिक्षाओं पर छात्रों और कॉर्पोरेट नेताओं के लिए परिवर्तनकारी प्रशिक्षण सत्र प्रदान किए हैं।'},
    {"name": 'गुरलीन कौर चावला', "email": 'gurleenkaur89998@gmail.com', "slug": 'gurleen-kaur-chawla', "designation": 'कंटेंट एडिटर', "description": 'फाइनेंस राइटर और एडिटर, जिन्हें बाज़ारों को सार्थक बनाने का जुनून है। मैं मैक्रोइकॉनॉमिक बदलावों से लेकर यह तक सब कुछ कवर करती हूं कि वे चुपचाप आम आदमी की जेब को कैसे प्रभावित करते हैं — क्योंकि अच्छी वित्तीय कहानी केवल आंकड़ों की नहीं, बल्कि लोगों की होती है।\r\nएनएमआईएमएस से फाइनेंस में एमबीए और वित्तीय शोध व संपादन में व्यावहारिक अनुभव के साथ, मैं हर लेख में विश्लेषणात्मक कठोरता और स्पष्ट कथा शैली लाती हूं। मैं वित्तीय पेशेवरों — फंड मैनेजर्स, एनालिस्ट्स और उद्योग जगत के नेताओं — का साक्षात्कार भी लेती हूं ताकि उनकी अंतर्दृष्टि व्यापक दर्शकों तक पहुंचाई जा सके।\r\nवर्तमान में कैपिटल मार्केट्स, इन्वेस्टमेंट रिसर्च और वित्तीय पत्रकारिता के संगम की खोज कर रही हूं।'},
    {"name": 'निर्मल', "email": 'nirmal@corporateimpact.in', "slug": 'nirmal', "designation": 'संपादक', "description": 'कॉर्पोरेट इम्पैक्ट में संपादक'},
    {"name": 'खुशबू अग्रहरी', "email": 'rash92chawla@gmail.com', "slug": 'khushboo-agrahari', "designation": 'संपादक', "description": 'खुशबू अग्रहरी चेन्नई, भारत में स्थित एक पत्रकार, लेखिका, पुस्तक समीक्षक और आलोचक हैं। उनका काम कई राष्ट्रीय और अंतरराष्ट्रीय प्रकाशनों में प्रकाशित हो चुका है, जहां उन्होंने विभिन्न विषयों पर लेख, समीक्षाएं, विशेष साक्षात्कार और टिप्पणियां दी हैं।'},
]

for auth in authors_data:
    if not auth["email"]:
        continue
    a, created = Author.objects.get_or_create(
        email=auth["email"],
        defaults={
            "name": auth["name"],
            "designation": auth["designation"],
            "slug": auth["slug"] or slugify(auth["name"], allow_unicode=True),
            "description": auth["description"]
        }
    )
    if not created:
        a.name = auth["name"]
        a.designation = auth["designation"]
        a.description = auth["description"]
        a.save()
    print(f"Author {auth['name']}: {'Created' if created else 'Updated'}")

print("\nSeeding Team...")
team_data = [
    {"name": 'गुरबीर सिंह चावला', "designation": 'मीडिया उद्यमी और समूह संपादक', "display_order": 1},
    {"name": 'रश्मीत कौर चावला', "designation": 'एक्ज़ीक्यूटिव एडिटर', "display_order": 2},
    {"name": 'प्रियंका चंदानी', "designation": 'एसोसिएट एडिटर', "display_order": 3},
    {"name": 'प्राची गुप्ता', "designation": 'एसोसिएट एडिटर', "display_order": 4},
    {"name": 'स्वेताक्षी लता', "designation": 'कंटेंट डेवलपमेंट एक्ज़ीक्यूटिव', "display_order": 5},
    {"name": 'अंशिका भारद्वाज', "designation": 'कंटेंट डेवलपमेंट डायरेक्टर', "display_order": 6},
]

for idx, t_data in enumerate(team_data):
    t, created = team.objects.get_or_create(
        name=t_data["name"],
        defaults={
            "designation": t_data["designation"],
            "display_order": t_data["display_order"] if t_data["display_order"] is not None else (idx + 1),
            "status": "Enabled"
        }
    )
    if not created:
        t.designation = t_data["designation"]
        t.display_order = t_data["display_order"] if t_data["display_order"] is not None else (idx + 1)
        t.save()
    print(f"Team Member {t_data['name']}: {'Created' if created else 'Updated'}")

print("\nSeeding Complete!")
