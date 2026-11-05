import streamlit as st

# ==========================================
# 1. SAYFA YAPILANDIRMASI VE GÜVENLİK/STİL
# ==========================================
st.set_page_config(
    page_title="Manevi Şifa ve Umut Portalı | Spiritual Healing",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kopyalamayı, sağ tıklamayı ve metin seçimini tamamen engelleyen CSS ve JS enjeksiyonu
st.markdown("""
    <style>
    /* Metin Seçimini ve İşaretlemeyi Tamamen Engelle */
    * {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
        -webkit-touch-callout: none !important;
    }
    
    /* Filigran (Watermark) */
    .watermark {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(-30deg);
        opacity: 0.03;
        font-size: 70px;
        font-weight: bold;
        color: #000;
        pointer-events: none;
        z-index: 9999;
        white-space: nowrap;
    }

    /* Kart Tasarımları */
    .card-box {
        background-color: #f8f9fa;
        border-left: 5px solid #2e7d32;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .card-title {
        color: #1b5e20;
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .card-text-tr {
        font-size: 1.05rem;
        color: #212529;
        margin-bottom: 8px;
        font-style: normal;
    }
    .card-text-en {
        font-size: 0.95rem;
        color: #495057;
        font-style: italic;
        margin-bottom: 12px;
    }
    .card-source {
        font-size: 0.85rem;
        color: #6c757d;
        font-weight: 600;
        text-align: right;
        border-top: 1px solid #e9ecef;
        padding-top: 8px;
    }
    
    /* Yazdırma Koruması */
    @media print {
        body { display: none !important; }
    }
    </style>

    <!-- Sağ Tık, Kısayol ve Geliştirici Araçları Engelleme -->
    <script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    
    document.addEventListener('keydown', function(e) {
        if (e.key === 'F12' || 
            (e.ctrlKey && (e.key === 'c' || e.key === 'C' || e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P' || e.key === 'a' || e.key === 'A' || e.key === 'i' || e.key === 'I'))) {
            e.preventDefault();
            alert("Güvenlik Politikası: Bu yazılımdaki içeriklerin kopyalanması, incelenmesi ve ticari kullanımı kesinlikle yasaktır.");
            return false;
        }
    });

    document.addEventListener('copy', function(e) {
        e.preventDefault();
        alert("İçerik Koruması: Metin kopyalamak yasaktır.");
    });
    </script>

    <div class="watermark">TİCARİ KULLANILAMAZ • MANEVİ DESTEK PORTALI</div>
""", unsafe_allow_html=True)


# ==========================================
# 2. VERİ KÜTÜPHANESİ (EKSİKSİZ 80 KAYIT)
# ==========================================
DATA = [
    # ------------------ AYETLER (20 ADET) ------------------
    {"cat": "Ayet", "tr": "Hastalandığım zaman bana şifa veren O'dur.", "en": "And when I am ill, it is He who cures me.", "src": "Şuarâ Sûresi, 26/80"},
    {"cat": "Ayet", "tr": "Şüphesiz güçlükle beraber bir kolaylık vardır.", "en": "Indeed, with hardship will come ease.", "src": "İnşirâh Sûresi, 94/6"},
    {"cat": "Ayet", "tr": "Allah kimseye taşıyabileceğinden fazlasını yüklemez.", "en": "Allah does not burden a soul beyond that it can bear.", "src": "Bakara Sûresi, 2/286"},
    {"cat": "Ayet", "tr": "Sabredenlere mükafatları hesapsız ödenecektir.", "en": "Indeed, the patient will be given their reward without account.", "src": "Zümer Sûresi, 39/10"},
    {"cat": "Ayet", "tr": "Biz Kur'an'dan, müminler için şifa ve rahmet olan şeyleri indiriyoruz.", "en": "And We send down of the Quran that which is healing and mercy for the believers.", "src": "İsrâ Sûresi, 17/82"},
    {"cat": "Ayet", "tr": "De ki: O, iman edenler için bir hidayet ve şifadır.", "en": "Say, 'It is, for those who believe, a guidance and cure.'", "src": "Fussilet Sûresi, 41/44"},
    {"cat": "Ayet", "tr": "Ey insanlar! Size Rabbimizden bir öğüt, gönüllerde olana bir şifa geldi.", "en": "O mankind, there has come to you instruction from your Lord and healing for what is in the breasts.", "src": "Yûnus Sûresi, 10/57"},
    {"cat": "Ayet", "tr": "Eğer Allah sana bir zarar dokundurursa, O'ndan başka bunu kaldıracak yoktur.", "en": "And if Allah should touch you with adversity, there is no remover of it except Him.", "src": "En'âm Sûresi, 6/17"},
    {"cat": "Ayet", "tr": "Rabbinize yalvara yakara ve gizlice dua edin.", "en": "Call upon your Lord in humility and in secret.", "src": "A'râf Sûresi, 7/55"},
    {"cat": "Ayet", "tr": "Bana dua edin, size cevap vereyim.", "en": "Call upon Me; I will respond to you.", "src": "Mü'min Sûresi, 40/60"},
    {"cat": "Ayet", "tr": "Rabbinin rahmetinden ancak sapıklar ümidini keser.", "en": "And who despairs of the mercy of his Lord except the misguided?", "src": "Hicr Sûresi, 15/56"},
    {"cat": "Ayet", "tr": "Allah sabredenlerle beraberdir.", "en": "Indeed, Allah is with the patient.", "src": "Bakara Sûresi, 2/153"},
    {"cat": "Ayet", "tr": "Şüphesiz Rabbim duayı işitendir.", "en": "Indeed, my Lord is the Hearer of supplication.", "src": "İbrâhîm Sûresi, 14/39"},
    {"cat": "Ayet", "tr": "Bilin ki, kalpler ancak Allah'ı anmakla huzur bulur.", "en": "Unquestionably, by the remembrance of Allah hearts find rest.", "src": "Ra'd Sûresi, 13/28"},
    {"cat": "Ayet", "tr": "Eyyûb da: 'Başıma bir dert geldi, sen merhametlilerin en merhametlisisin' diye nida etmişti.", "en": "And Job, when he called to his Lord, 'Indeed, adversity has touched me, and You are the Most Merciful.'", "src": "Enbiyâ Sûresi, 21/83"},
    {"cat": "Ayet", "tr": "Biz de onun duasını kabul ettik ve kendisindeki sıkıntıyı kaldırdık.", "en": "So We responded to him and removed what afflicted him of adversity.", "src": "Enbiyâ Sûresi, 21/84"},
    {"cat": "Ayet", "tr": "O, benim dualarımı işitendir ve bana yakın olandır.", "en": "Indeed, He is Hearing and near.", "src": "Sebe' Sûresi, 34/50"},
    {"cat": "Ayet", "tr": "De ki: Allah'ın bizim için yazdığından başkası bize asla erişmez. O bizim mevlamızdır.", "en": "Say, 'Never will we be struck except by what Allah has decreed for us; He is our protector.'", "src": "Tevbe Sûresi, 9/51"},
    {"cat": "Ayet", "tr": "Nice az topluluklar Allah'ın izniyle büyük topluluklara galip gelmiştir.", "en": "How many a small company has overcome a large company by permission of Allah.", "src": "Bakara Sûresi, 2/249"},
    {"cat": "Ayet", "tr": "Ben hüznümü ve kederimi ancak Allah'a arz ederim.", "en": "I only complain of my suffering and my grief to Allah.", "src": "Yûsuf Sûresi, 12/86"},

    # ------------------ HADİSLER (20 ADET) ------------------
    {"cat": "Hadis", "tr": "Ey Allah'ın kulları! Tedavi olunuz. Çünkü Allah yarattığı her hastalığın şifasını da yaratmıştır.", "en": "O servants of Allah, seek treatment, for Allah has created a cure for every disease He created.", "src": "Ebu Davud, Tıb 1 (2015/3855)"},
    {"cat": "Hadis", "tr": "Müslümana yorgunluk, hastalık, kaygı, hüzün, eziyet ve kederden ne isabet ederse olsun, hatta ayağına batan dikene varıncaya kadar, Allah bunlarla onun günahlarını bağışlar.", "en": "No fatigue, nor disease, nor sorrow, nor sadness, nor hurt, nor distress befalls a Muslim, even if it were the prick he receives from a thorn, but that Allah expiates some of his sins for that.", "src": "Buhârî, المرضى 1; Müslim, Birr 52"},
    {"cat": "Hadis", "tr": "Müminin durumu ne hoştur! Her hali kendisi için hayırdır. Bu durum yalnız mümine hastır. Başına sevinecek bir iş gelse şükreder, bu onun için hayır olur. Başına bir sıkıntı gelse sabreder, bu da onun için hayır olur.", "en": "How wonderful is the affair of the believer, for his affairs are all good, and this applies to no one but the believer. If something good happens to him, he is thankful, and that is good for him. If something bad happens to him, he bears it with patience, and that is good for him.", "src": "Müslim, Zühd 64 (2999)"},
    {"cat": "Hadis", "tr": "Allah bir kuluna hayır murad ederse, cezasını dünyada peşin verir.", "en": "When Allah intends good for His servant, He punishes him in this world.", "src": "Tirmizî, Zühd 57 (2396)"},
    {"cat": "Hadis", "tr": "Mükafatın büyüklüğü, belanın büyüklüğüyle orantılıdır.", "en": "The magnitude of the reward is proportional to the magnitude of the affliction.", "src": "Tirmizî, Zühd 57 (2396)"},
    {"cat": "Hadis", "tr": "Hastalık günahları temizler, tıpkı demircinin körüğünün demirin kirini temizlediği gibi.", "en": "Sickness expiates sins, just as a blacksmith's bellows remove impurities from iron.", "src": "İbn Majah, Tıb 18"},
    {"cat": "Hadis", "tr": "Hastaları ziyaret ediniz ve onlardan dua isteyiniz. Çünkü hastanın duası meleklerin duası gibidir.", "en": "Visit the sick and ask them for prayers, for the prayer of the sick person is like that of the angels.", "src": "İbn Majah, Cenz 2"},
    {"cat": "Hadis", "tr": "Gözleri görmez olan kuluma sabrederse, ona cenneti veririm.", "en": "If My servant endures the loss of his two beloved eyes with patience, I shall compensate him with Paradise.", "src": "Buhârî, المرضى 7"},
    {"cat": "Hadis", "tr": "Allah, şifasını vermediği hiçbir hastalığı indirmemiştir.", "en": "Allah has not sent down any disease without sending down a cure for it.", "src": "Buhârî, Tıb 1"},
    {"cat": "Hadis", "tr": "Sadaka vermek hastalarınızı tedavi eder ve belaları defeder.", "en": "Treat your sick ones with charity and ward off afflictions.", "src": "Kenzu'l-Ummal, 6/371"},
    {"cat": "Hadis", "tr": "Sıkıntı zamanlarında Allah'a dua etmekten hoşlanan kimse, bolluk anında da duasını çoğaltsın.", "en": "Whoever wishes that Allah would respond to him during hardship and grief, let him supplicate much in times of ease.", "src": "Tirmizî, Daavât 9"},
    {"cat": "Hadis", "tr": "Ey insanların Rabbi! Sıkıntıyı gider, şifa ver. Şifa veren ancak sensin.", "en": "O Lord of mankind, remove the suffering and heal, for You are the Healer.", "src": "Buhârî, المرضى 20"},
    {"cat": "Hadis", "tr": "Hiçbiriniz başına gelen bir sıkıntıdan dolayı ölümü temenni etmesin.", "en": "None of you should wish for death because of a hardship that has befallen him.", "src": "Buhârî, المرضى 19"},
    {"cat": "Hadis", "tr": "Duaların en hayırlısı, hamd ve şükür ile yapılan duadır.", "en": "The best supplication is that made with praise and gratitude.", "src": "Tirmizî, Daavât 1"},
    {"cat": "Hadis", "tr": "Bir mümin hasta olduğunda, Allah onun günahlarını sonbahar yapraklarının döküldüğü gibi döker.", "en": "When a believer falls ill, Allah sheds his sins just as autumn leaves fall from a tree.", "src": "Buhârî, المرضى 13"},
    {"cat": "Hadis", "tr": "Kul hasta olduğu zaman, Allah ona iki melek gönderir ve 'Bakın görün, kulum ziyaretçilerine ne diyor' der.", "en": "When a servant falls ill, Allah sends two angels to see what he says to his visitors.", "src": "Muvatta, Ayn 12"},
    {"cat": "Hadis", "tr": "Hastalık, kulun ruhunu arındıran manevi bir banyodur.", "en": "Illness is a spiritual bath that purifies the soul of a servant.", "src": "Tirmizî, Zühd 56"},
    {"cat": "Hadis", "tr": "Kim bir hastayı akşamleyin ziyaret ederse, onunla birlikte yetmiş bin melek sabaha kadar bağışlanma diler.", "en": "Whoever visits a sick person in the evening, seventy thousand angels pray for his forgiveness until morning.", "src": "Ebu Davud, Cenâiz 3"},
    {"cat": "Hadis", "tr": "Şifa üç şeydedir: Bal şerbeti içmek, hacamat yaptırmak ve dağlanmak. Ancak ümmetime dağlanmayı yasaklarım.", "en": "Healing is in three things: A gulp of honey, cupping, and cauterization. But I forbid my followers to use cauterization.", "src": "Buhârî, Tıb 3"},
    {"cat": "Hadis", "tr": "Sabır, ilk darbe anında gösterilendir.", "en": "Patience is only at the first stroke of a calamity.", "src": "Buhârî, Cenâiz 32"},

    # ------------------ HİKMETLİ SÖZLER (20 ADET) ------------------
    {"cat": "Hikmetli Sözler", "tr": "Hastalık, bedenin zekatıdır; ruhu saflaştırır ve insanı gururdan korur.", "en": "Sickness is the zakat of the body; it purifies the soul and protects man from pride.", "src": "Şeyh Abdülkadir Geylânî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Üzülme! Çünkü dert, Allah'ı gizlice çağırmanın beyanadır. Dermanı arayan derttir.", "en": "Do not grieve! For trouble is the declaration of calling Allah secretly. It is pain that seeks the remedy.", "src": "Mevlânâ Celâleddîn-i Rûmî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Sağlık bir taçtır ki, onu ancak hastalar görebilir.", "en": "Health is a crown that only the sick can see.", "src": "İmam-ı Gazâlî (r.a.)"},
    {"cat": "Hikmetli Sözler", "tr": "Kahru lütfu şey-i vahid bilmeyen çekmedi vahdet şarabından çeşni.", "en": "He who does not see wrath and grace as one has not tasted the wine of divine unity.", "src": "Yunus Emre"},
    {"cat": "Hikmetli Sözler", "tr": "Hastalık sana Rabbinin bir iltifatıdır; seni dünyevi meşguliyetlerden çekip Kendi huzuruna çağırır.", "en": "Illness is a compliment from your Lord; it pulls you away from worldly distractions and invites you into His presence.", "src": "Ahmad Ibn Ataullah al-Iskandari (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Her dert bir imtihandır; sabredersen rütbe, feryat edersen yük olur.", "en": "Every trouble is a test; if you endure, it becomes a rank; if you lament, it becomes a burden.", "src": "Hasan-ı Basrî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Gözü hüzünlü olanın kalbi nurlu olur. Hastalık kalbin aydınlığına vesiledir.", "en": "He whose eyes are sad, his heart becomes luminous. Illness leads to the enlightenment of the heart.", "src": "Fudayl bin İyâz (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Beden hastalanınca yemekten tat almaz; kalp hastalanınca da ibadetten tat almaz.", "en": "When the body is sick, it finds no taste in food; when the heart is sick, it finds no taste in worship.", "src": "Zünnûn-ı Mısrî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Rabbinden gelen her şeye 'Eyvallah' diyebilmek, şifanın ilk basamağıdır.", "en": "Accepting everything that comes from your Lord is the first step to healing.", "src": "Aziz Mahmud Hüdayi (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Sabır, boyun eğmek değil; mücadelesini sessizce ve tevekkülle sürdürmektir.", "en": "Patience is not submission; it is continuing the struggle quietly and with trust in God.", "src": "İmam Rabbani (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Hastalığın acısı geçicidir, fakat kazandırdığı sevap ve olgunluk bakidir.", "en": "The pain of illness is temporary, but the reward and maturity it brings are eternal.", "src": "Bişr-i Hafi (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Kaza ve kadere rıza göstermek, ruhun en büyük şifasıdır.", "en": "Contentment with divine decree is the greatest healing for the soul.", "src": "Şah-ı Nakşibend (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Duaların kabul olacağı en mükemmel an, acizlik ve çaresizliğin iliklere kadar hissedildiği andır.", "en": "The most perfect moment for prayers to be accepted is when helplessness is felt to the core.", "src": "İbrahim bin Ethem (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Bedenin hastalığı günahlara kefarettir; kalbin hastalığı ise gaflettir.", "en": "Physical illness is an expiation for sins; illness of the heart is heedlessness.", "src": "Sırrı-yı Sekatî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Acı çekmek ruhun uyanışıdır; fani dünyanın hakikatini anlatır.", "en": "Suffering is the awakening of the soul; it tells the truth of the mortal world.", "src": "Mevlânâ Celâleddîn-i Rûmî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Hastalık zamanı tefekkür zamanıdır. İnsan acziyetini anlar, Yaratanına yönelir.", "en": "Time of illness is time of reflection. Man realizes his weakness and turns to his Creator.", "src": "İmam Süyûtî (r.a.)"},
    {"cat": "Hikmetli Sözler", "tr": "Derdin kendisi sana derman olmaya gelmiştir, yeter ki ibret nazarıyla bakmayı bil.", "en": "The trouble itself came to be your cure, as long as you look at it with lesson-seeking eyes.", "src": "Niyâzî-i Mısrî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Allah'ın takdirine teslim olan, dünyevi ızdıraplardan azad olur.", "en": "He who surrenders to the decree of Allah is freed from worldly suffering.", "src": "Cüneyd-i Bağdâdî (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Bela ve musibetler dostların kamçısıdır; onları Hak kapısına sevk eder.", "en": "Tribulations are the whip of friends; they drive them to the door of Truth.", "src": "Ebu Said el-Harraz (k.s.)"},
    {"cat": "Hikmetli Sözler", "tr": "Kalbinde Allah sevgisi olanın, bedenindeki dertler ruhuna ağırlık vermez.", "en": "He who has love of Allah in his heart, the troubles of the body do not weigh on his soul.", "src": "Yahya bin Muaz (k.s.)"},

    # ------------------ HASTALAR RİSALESİ (20 ADET) ------------------
    {"cat": "Hastalar Risalesi", "tr": "Ey hasta kardeş! Hastalık senin hayatını tasfiye eder, günahlarını döker ve ömrünü ibadet hükmüne getirir.", "en": "O sick brother! Sickness purifies your life, sheds your sins, and makes your life count as worship.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (1. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık sabır ile karşılanırsa, insanın ömrünün her bir saati bir gün ibadet hükmüne geçer.", "en": "If sickness is met with patience, each hour of a person's life becomes equivalent to a day of worship.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (2. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "İnsan bu dünyaya keyif sürmek için gelmemiştir. İnsan, sermaye-i ömrünü ibadetle ticarete çevirmek için gelmiştir.", "en": "Man has not come into this world for pleasure; he has come to trade the capital of his life through worship.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (3. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık, sana acizlik ve zayıflığını bildirerek Rabbinin dergahına iltica etmeni sağlar.", "en": "Sickness makes you realize your helplessness and weakness, prompting you to seek refuge in your Lord's presence.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (4. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık, dünyadaki fani lezzetlerin acılığını gösterip insanı baki olan ahirete sevk eden bir ikazdır.", "en": "Sickness is a warning that shows the bitterness of mortal worldly pleasures and directs man to the eternal hereafter.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (5. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Şekva (şikayet) etmemek şartıyla, hastalık anında yapılan dualar makbuldür.", "en": "Provided there is no complaining, prayers offered during illness are highly acceptable.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (6. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık, sıhhatin kıymetini bildiren en tesirli bir öğretmendir.", "en": "Sickness is the most effective teacher that makes known the value of health.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (7. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Senin vücudun senin mülkün değildir; Şâfi-i Hakiki olan Allah'ın mülküdür. O, mülkünde istediği gibi tasarruf eder.", "en": "Your body is not your property; it belongs to Allah, the True Healer. He disposes of His property as He wills.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (8. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık günahlara keffaret olduğu gibi, kalbi ve ruhu dünyevi kirlerden temizler.", "en": "Just as sickness is an expiation for sins, it purifies the heart and soul from worldly stains.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (9. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Gözünü aç, arkana bak: Geçmiş zamanın lezzetleri gitmiş, ama çekilen zahmetlerin sevabı kalmıştır.", "en": "Open your eyes, look back: The pleasures of past times have vanished, but the rewards of troubles endure.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (10. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık sıhhatteki gafleti dağıtır, insana aczini hissettirip tam bir ubudiyet kazandırır.", "en": "Sickness dispels heedlessness in health, makes man feel his weakness, and confers true servitude.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (11. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Ey hasta! Hastalıktaki manevi lezzeti ve sevabı düşünsen, şifa istemekten çekinebilirsin.", "en": "O sick person! If you consider the spiritual pleasure and reward in sickness, you might hesitate to ask for healing.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (12. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık fani ömrü bakiye çevirir; fani lezzetlerin yerine baki meyveler verir.", "en": "Sickness turns mortal life into eternal life; it gives eternal fruits instead of mortal pleasures.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (13. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Şikayeti Allah'a yapmalı, Allah'tan şikayet etmemeli. Yani derdini O'na arz etmeli, kaderi suçlamamalı.", "en": "One should complain to Allah, not complain about Allah. That is, present your trouble to Him, do not blame fate.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (14. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık insandaki gurur ve kibiri kırar, onu alçakgönüllü ve samimi bir kul yapar.", "en": "Sickness breaks pride and arrogance in man, making him a humble and sincere servant.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (15. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Merhametli Yaratan'ın sana gönderdiği hediye-i hastalıktan şikayet etme; O'na tevekkül et.", "en": "Do not complain about the gift of sickness sent to you by the Merciful Creator; place your trust in Him.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (16. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık, kalbin ve ruhun inkişafına vesile olan manevi bir ameliyattır.", "en": "Sickness is a spiritual operation that occasions the development of the heart and soul.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (17. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Dünyanın en lezzetli anları bile geçicidir; ama sabırla çekilen dertlerin mükafatı daimidir.", "en": "Even the most delicious moments of the world are temporary; but the reward for endured troubles is eternal.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (18. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Hastalık seni Mevla'na yakınlaştırıyorsa, o bir hastalık değil, ilahi bir rahmettir.", "en": "If sickness brings you closer to your Lord, it is not a disease, but divine mercy.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (19. Deva)"},
    {"cat": "Hastalar Risalesi", "tr": "Ey sabırsız hasta! Sabret, hatta şükret. Çünkü senin bu hastalığın ömrünü ibadet kılacak bir iksirdir.", "en": "O impatient sick person! Be patient, even give thanks. For this illness of yours is an elixir that makes your life worship.", "src": "Bediüzzaman Said Nursi - Hastalar Risalesi (25. Deva)"}
]


# ==========================================
# 3. YARDIMCI FONKSİYONLAR
# ==========================================
def filter_records(category, keyword, lang_mode):
    filtered = []
    for item in DATA:
        if category != "Tümü / All" and item["cat"] != category:
            continue
        
        # Arama filtreleme
        if keyword:
            kw = keyword.lower()
            text_tr = item["tr"].lower()
            text_en = item["en"].lower()
            src = item["src"].lower()
            if kw not in text_tr and kw not in text_en and kw not in src:
                continue
                
        filtered.append(item)
    return filtered


# ==========================================
# 4. SOL YAN PANEL (SIDEBAR) & FİLTRELER
# ==========================================
with st.sidebar:
    st.header("🌿 Navigasyon & Filtreler")
    st.markdown("---")
    
    # Dil Seçimi
    lang_mode = st.radio(
        "Gösterim Dili / Display Language",
        ["Çift Dil (TR / EN)", "Sadece Türkçe", "English Only"],
        index=0
    )
    
    st.markdown("---")
    
    # Kategori Seçimi
    category = st.selectbox(
        "Kategori / Category",
        ["Tümü / All", "Ayet", "Hadis", "Hikmetli Sözler", "Hastalar Risalesi"]
    )
    
    # Kelime Arama
    keyword = st.text_input("Anahtar Kelime Ara / Search Keyword", placeholder="Örn: Sabır, Şifa, Healing...")
    
    st.markdown("---")
    
    # İstatistik Bilgisi
    filtered_data = filter_records(category, keyword, lang_mode)
    st.metric("Gösterilen Kayıt / Displayed Records", len(filtered_data))

    st.markdown("---")
    st.info("🔒 *Telif & Koruma uyarısı:* Metinler kopyalamaya karşı korunmaktadır. Ticari amaçla çoğaltılamaz.")

    # Kenar Çubuğuna Uyku Modu Bilgi Notu ve Yönlendirmesi
    st.markdown("---")
    st.sidebar.info(
        "💡 *Not:* Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. "
        "Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir "
        "(ekranda 'Zzzz' simgesi çıkabilir).\n\n"
        "💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli "
        "_'Yes, get this app back up!'_ butonuna tıklayın ve uygulamanın "
        "yeniden uyanması için 15-30 saniye bekleyin."
    )


# ==========================================
# 5. ANA EKRAN VE BAŞLIK
# ==========================================
st.title("🌱 Manevi Şifa ve Umut Portalı")
st.subheader("Spiritual Healing & Hope Portal for Patients")

st.markdown("""
> Bu portal, rahatsızlık geçiren kardeşlerimize manevi moral, sabır, metanet ve şifa kaynağı olmak amacıyla derlenmiştir.
""")

st.markdown("---")


# ==========================================
# 6. İÇERİK KARTLARININ LİSTELENMESİ
# ==========================================
if not filtered_data:
    st.warning("Aramanıza uygun bir kayıt bulunamadı. Lütfen arama terimini değiştirin.")
else:
    for idx, item in enumerate(filtered_data, 1):
        # Kategoriye göre simge atama
        icon = "📖" if item["cat"] == "Ayet" else ("💬" if item["cat"] == "Hadis" else ("💡" if item["cat"] == "Hikmetli Sözler" else "📜"))
        
        # Kart şablonunu oluşturma
        content_html = f"""
        <div class="card-box">
            <div class="card-title">{icon} {item['cat']} - #{idx}</div>
        """
        
        if lang_mode in ["Çift Dil (TR / EN)", "Sadece Türkçe"]:
            content_html += f'<div class="card-text-tr">"{item["tr"]}"</div>'
            
        if lang_mode in ["Çift Dil (TR / EN)", "English Only"]:
            content_html += f'<div class="card-text-en">"{item["en"]}"</div>'
            
        content_html += f"""
            <div class="card-source">📌 Kaynak / Source: {item['src']}</div>
        </div>
        """
        
        st.markdown(content_html, unsafe_allow_html=True)


# ==========================================
# 7. ALT BİLGİ & HUKUKİ BİLDİRİM (DISCLAIMER)
# ==========================================
st.markdown("---")

st.markdown("""
<div style="background-color: #fff3cd; border: 1px solid #ffeeba; color: #856404; padding: 15px; border-radius: 5px; font-size: 0.85rem;">
    <h4>⚖️ Hukuki Bildirim, Lisans ve Şartlar / Legal Disclaimer & Terms</h4>
    <p><strong>1. Amaç ve Kapsam:</strong> Bu yazılım ve içerisindeki derlemeler tamamen manevi destek, bilgi, moral ve kişisel gelişim amacıyla hazırlanmıştır. Tıbbi teşhis, tedavi veya tıbbi tavsiye yerine geçmez. Sağlık sorunlarınız için mutlaka uzman bir hekime başvurunuz.</p>
    <p><strong>2. Ticari Kullanım Yasağı:</strong> Bu yazılım, kod yapısı ve içerdiği veri kütüphanesi hiçbir şekilde satılamaz, ticari bir faaliyete konu edilemez, gelir elde etmek amacıyla kullanılamaz.</p>
    <p><strong>3. Kopyalama ve Çoğaltma Yasağı:</strong> Yazılım içerisindeki verilerin ve kod yapısının izinsiz kopyalanması, çoğaltılması, başka platformlara aktarılması veya dağıtılması hukuki koruma altındadır ve yasaktır.</p>
    <p><em>© Tüm Hakları Saklıdır. Manevi gelişim ve şifa amacıyla serbestçe görüntülenebilir.</em></p>
</div>
""", unsafe_allow_html=True)