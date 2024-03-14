v = "ECC"
panel_label = v
panel_name  = v.upper()
array_name = f"array_{v.lower()}"

array = [
# ["Class Name","Tool Tip","Button Label","ID Name","Hex Color"],
["Audi_Nardo_Grey","Audi's classic grey color","Nardo Grey","audi_nardo_grey","C0C6C8"],
["Ferrari_Argento_Nurburgring","Ferrari's metallic silver color","Argento Nurburgring","ferrari_argento_nurburgring","CACBCE"],
["Ferrari_Bianco_Avorio","Ferrari's cream white color","Bianco Avorio","ferrari_bianco_avorio","E5DEDC"],
["Ferrari_Bianco_Avus","Ferrari's classic white color","Bianco Avus","ferrari_bianco_avus","F2F3F6"],
["Ferrari_Blu_Abu_Dhabi","Ferrari's light blue color","Blu Abu Dhabi","ferrari_blu_abu_dhabi","2885B5"],
["Ferrari_Blu_Pozzi","Ferrari's deep blue color","Blu Pozzi","ferrari_blu_pozzi","2C3970"],
["Ferrari_Blu_Scozia","Ferrari's dark blue color","Blu Scozia","ferrari_blu_scozia","505C77"],
["Ferrari_Blu_Swaters","Ferrari's royal blue color","Blu Swaters","ferrari_blu_swaters","163166"],
["Ferrari_Blu_Tour_De_France","Ferrari's classic blue color","Blu Tour De France","ferrari_blu_tour_de_france","2243AA"],
["Ferrari_Canna_Di_Fucile","Ferrari's metallic grey color","Canna Di Fucile","ferrari_canna_di_fucile","7E8792"],
["Ferrari_Giallo_Modena","Ferrari's triple layer yellow color","Giallo Modena","ferrari_giallo_modena","FCE903"],
["Ferrari_Grigio_Alloy","Ferrari's light grey (blue) color","Grigio Alloy","ferrari_grigio_alloy","A3C7E9"],
["Ferrari_Grigio_Ferro","Ferrari's light grey color","Grigio Ferro","ferrari_grigio_ferro","626062"],
["Ferrari_Grigio_Ingrid","Ferrari's beige grey color","Grigio Ingrid","ferrari_grigio_ingrid","756D62"],
["Ferrari_Grigio_Scuro","Ferrari's deep grey color","Grigio Scuro","ferrari_grigio_scuro","4C4E4D"],
["Ferrari_Grigio_Silverstone","Ferrari's dark grey color","Grigio Silverstone","ferrari_grigio_silverstone","585C64"],
["Ferrari_Grigio_Titanio","Ferrari's classic grey color","Grigio Titanio","ferrari_grigio_titanio","A8B8C0"],
["Ferrari_Nero_Daytona","Ferrari's classic black color","Nero Daytona","ferrari_nero_daytona","231F1C"],
["Ferrari_Rosso_70_Anni","Ferrari's 70th anniversary celebration color","Rosso 70 Anni","ferrari_rosso_70_anni","C40C19"],
["Ferrari_Rosso_Corsa","Ferrari's classic red color","Rosso Corsa","ferrari_rosso_corsa","D40000"],
["Ferrari_Rosso_Dino","Ferrari's red/orange color","Rosso Dino","ferrari_rosso_dino","FC652E"],
["Ferrari_Rosso_Fiorano","Ferrari's ruby red color","Rosso Fiorano","ferrari_rosso_fiorano","5D0001"],
["Ferrari_Rosso_Fuoco","Ferrari's triple layer red color","Rosso Fuoco","ferrari_rosso_fuoco","D13442"],
["Ferrari_Rosso_Mugello","Ferrari's dark red color","Rosso Mugello","ferrari_rosso_mugello","7A212A"],
["Ferrari_Rosso_Scuderia","Ferrari's bright red color","Rosso Scuderia","ferrari_rosso_scuderia","ff2800"],
["Ferrari_Verde_British","Ferrari's British racing green color","Verde British","ferrari_verde_british","004225"],
["Lamborghini_Arancia_Atlas","Lamborghini's shiny orange color","Arancia Atlas","lamborghini_arancia_atlas","FC9303"],
["Lamborghini_Arancio_Argos","Lamborghini's Ad Personam fire red color","Arancio Argos","lamborghini_arancio_argos","FB6445"],
["Lamborghini_Arancio_Borealis","Lamborghini's Ad Personam orange color","Arancio Borealis","lamborghini_arancio_borealis","FBA400"],
["Lamborghini_Arancio_Bruciato","Lamborghini's contemporary orange color","Arancio Bruciato","lamborghini_arancio_bruciato","D74C10"],
["Lamborghini_Arancio_Xanto","Lamborghini's sportiva orange color","Arancio Xanto","lamborghini_arancio_xanto","E64A37"],
["Lamborghini_Azzurro_Thetys","Lamborghini's Ad Personam light blue color","Azzurro Thetys","lamborghini_azzurro_thetys","8CA0B8"],
["Lamborghini_Balloon_White","Lamborghini's contemporary white color","Balloon White","lamborghini_balloon_white","E8E8E8"],
["Lamborghini_Bianco_Asopo","Lamborghini's sportiva white color","Bianco Asopo","lamborghini_bianco_asopo","F3FAFD"],
["Lamborghini_Bianco_Comes","Lamborghini's pearl white color","Bianco Comes","lamborghini_bianco_comes","FBFBFB"],
["Lamborghini_Bianco_Isi","Lamborghini's shiny white color","Bianco Isi","lamborghini_bianco_isi","C0CBCD"],
["Lamborghini_Bianco_Monocerus","Lamborghini's Ad Personam white color","Bianco Monocerus","lamborghini_bianco_monocerus","EDEDED"],
["Lamborghini_Blu_Aegir","Lamborghini's contemporary blue color","Blu Aegir","lamborghini_blu_aegir","2CAEFE"],
["Lamborghini_Blu_Astraeus","Lamborghini's Ad Personam deep blue color","Blu Astraeus","lamborghini_blu_astraeus","00024C"],
["Lamborghini_Blu_Caelum","Lamborghini's Ad Personam royal blue color","Blu Caelum","lamborghini_blu_caelum","054AE3"],
["Lamborghini_Blu_Cepheus","Lamborghini's pearl blue color","Blu Cepheus","lamborghini_blu_cepheus","39BFFE"],
["Lamborghini_Blu_Eleos","Lamborghini's Ad Personam shiny blue color","Blu Eleos","lamborghini_blu_eleos","418DD8"],
["Lamborghini_Blu_Fontus","Lamborghini's Ad Personam dark blue color","Blu Fontus","lamborghini_blu_fontus","313247"],
["Lamborghini_Blu_Glauco","Lamborghini's Ad Personam teal color","Blu Glauco","lamborghini_blu_glauco","08C7E3"],
["Lamborghini_Blu_Le_Mans","Lamborghini's Ad Personam bright blue color","Blu Le Mans","lamborghini_blu_le_mans","0690FF"],
["Lamborghini_Blu_Nereid","Lamborghini's Ad Personam metallic blue color","Blu Nereid","lamborghini_blu_nereid","2539BC"],
["Lamborghini_Blu_Nethuns","Lamborghini's sportiva blue color","Blu Nethuns","lamborghini_blu_nethuns","1336EA"],
["Lamborghini_Blu_Nila","Lamborghini's shiny blue color","Blu Nila","lamborghini_blu_nila","017EF4"],
["Lamborghini_Blu_Notte","Lamborghini's classic blue color","Blu Notte","lamborghini_blu_notte","212E58"],
["Lamborghini_Blu_Uranus","Lamborghini's pearl ocean color","Blu Uranus","lamborghini_blu_uranus","0177A4"],
["Lamborghini_Bronzo_Zante","Lamborghini's contemporary bronze color","Bronzo Zante","lamborghini_bronzo_zante","B08D57"],
["Lamborghini_Giallo_Auge","Lamborghini's Ad Personam yellow color","Giallo Auge","lamborghini_giallo_auge","FEBE05"],
["Lamborghini_Giallo_Evros","Lamborghini's Ad Personam dark yellow color","Giallo Evros","lamborghini_giallo_evros","E28F01"],
["Lamborghini_Giallo_Inti","Lamborghini's Ad Personam bright yellow color","Giallo Inti","lamborghini_giallo_inti","FED136"],
["Lamborghini_Giallo_Orion","Lamborghini's shiny yellow color","Giallo Orion","lamborghini_giallo_orion","FEA700"],
["Lamborghini_Giallo_Spica","Lamborghini's Ad Personam pearl yellow color","Giallo Spica","lamborghini_giallo_spica","F2C32F"],
["Lamborghini_Giallo_Tenerife","Lamborghini's Ad Personam pale yellow color","Giallo Tenerife","lamborghini_giallo_tenerife","F2F427"],
["Lamborghini_Grigio_Antares","Lamborghini's Ad Personam metallic grey color","Grigio Antares","lamborghini_grigio_antares","A6ADB7"],
["Lamborghini_Grigio_Ater","Lamborghini's Ad Personam dark grey color","Grigio Ater","lamborghini_grigio_ater","727274"],
["Lamborghini_Grigio_Estoque","Lamborghini's Ad Personam metallic grey color","Grigio Estoque","lamborghini_grigio_estoque","ACACAE"],
["Lamborghini_Grigio_Hati","Lamborghini's Ad Personam light grey color","Grigio Hati","lamborghini_grigio_hati","C7D7E7"],
["Lamborghini_Grigio_Keres","Lamborghini's Ad Personam metallic grey color","Grigio Keres","lamborghini_grigio_keres","6F6F6F"],
["Lamborghini_Grigio_Liqueo","Lamborghini's Ad Personam light metallic grey color","Grigio Liqueo","lamborghini_grigio_liqueo","85898D"],
["Lamborghini_Grigio_Lynx","Lamborghini's Ad Personam grey color","Grigio Lynx","lamborghini_grigio_lynx","707176"],
["Lamborghini_Grigio_Nimbus","Lamborghini's Ad Personam bright light grey color","Grigio Nimbus","lamborghini_grigio_nimbus","6B7278"],
["Lamborghini_Grigio_Telesto","Lamborghini's sportiva grey color","Grigio Telesto","lamborghini_grigio_telesto","7692A5"],
["Lamborghini_Nero_Aldebaran","Lamborghini's shiny black color","Nero Aldebaran","lamborghini_nero_aldebaran","0D1015"],
["Lamborghini_Nero_Granatus","Lamborghini's contemporary black color","Nero Granatus","lamborghini_nero_granatus","92555D"],
["Lamborghini_Nero_Helene","Lamborghini's Ad Personam black color","Nero Helene","lamborghini_nero_helene","151618"],
["Lamborghini_Nero_Nemesis","Lamborghini's Ad Personam matte black color","Nero Nemesis","lamborghini_nero_nemesis","312F30"],
["Lamborghini_Nero_Noctis","Lamborghini's Ad Personam metallic black color","Nero Noctis","lamborghini_nero_noctis","292927"],
["Lamborghini_Nero_Pegaso","Lamborghini's Ad Personam dark black color","Nero Pegaso","lamborghini_nero_pegaso","080D10"],
["Lamborghini_Oros_Elios","Lamborghini's pearl bronze color","Oros Elios","lamborghini_oros_elios","B88B60"],
["Lamborghini_Rosso_Arancio","Lamborghini's classic red color","Rosso Arancio","lamborghini_rosso_arancio","DD3D0D"],
["Lamborghini_Rosso_Bia","Lamborghini's Ad Personam cherry red color","Rosso Bia","lamborghini_rosso_bia","C10001"],
["Lamborghini_Rosso_Efesto","Lamborghini's contemporary red color","Rosso Efesto","lamborghini_rosso_efesto","F4221F"],
["Lamborghini_Rosso_Leto","Lamborghini's Ad Personam deep red color","Rosso Leto","lamborghini_rosso_leto","B60035"],
["Lamborghini_Rosso_Mars","Lamborghini's shiny red color","Rosso Mars","lamborghini_rosso_mars","D40000"],
["Lamborghini_Verde_Citrea","Lamborghini's pearl green color","Verde Citrea","lamborghini_verde_citrea","9AF95D"],
["Lamborghini_Verde_Ermes","Lamborghini's Ad Personam dark green color","Verde Ermes","lamborghini_verde_ermes","546E51"],
["Lamborghini_Verde_Gea_Lucido","Lamborghini's contemporary green color","Verde Gea Lucido","lamborghini_verde_gea_lucido","8B8970"],
["Lamborghini_Verde_Ithaca","Lamborghini's Ad Personam bright green color","Verde Ithaca","lamborghini_verde_ithaca","AEFF7E"],
["Lamborghini_Verde_Mantis","Lamborghini's shiny green color","Verde Mantis","lamborghini_verde_mantis","7DC23B"],
["Lamborghini_Verde_Metallic","Lamborghini's classic british racing green color","Verde Metallic","lamborghini_verde_metallic","8FC028"],
["Lamborghini_Verde_Scandal","Lamborghini's classic green color","Verde Scandal","lamborghini_verde_scandal","84E12E"],
["Lamborghini_Verde_Selvans","Lamborghini's sportiva green color","Verde Selvans","lamborghini_verde_selvans","67C52F"],
["Lamborghini_Viola_30","Lamborghini's classic purple color","Viola 30","lamborghini_viola_30","B27CB6"],
["Lamborghini_Viola_Aletheia","Lamborghini's Ad Personam deep purple color","Viola Aletheia","lamborghini_viola_aletheia","492AC5"],
["Lamborghini_Viola_Pasifae","Lamborghini's sportiva purple color","Viola Pasifae","lamborghini_viola_pasifae","6B0686"],
["McLaren_Aurora_Blue","McLaren's deep blue color","Aurora Blue","mclaren_aurora_blue","172375"],
["McLaren_Cobalt_Violet","McLaren's dark purple color","Cobalt Violet","mclaren_cobalt_violet","C8659E"],
["McLaren_Curacao_Blue","McLaren's bright blue color","Curacao Blue","mclaren_curacao_blue","00B8EE"],
["McLaren_Fire_Black","McLaren's metallic black color","Fire Black","mclaren_fire_black","191A1E"],
["McLaren_Ice_Silver","McLaren's bright silver color","Ice Silver","mclaren_ice_silver","C4C8D4"],
["McLaren_Lantana_Purple","McLaren's deep purple color","Lantana Purple","mclaren_lantana_purple","351175"],
["McLaren_Lime_Green","McLaren's bright green color","Lime Green","mclaren_lime_green","C2ED3E"],
["McLaren_Mantis_Green","McLaren's bright green color","Mantis Green","mclaren_mantis_green","63EA2E"],
["McLaren_McLaren_Argon","McLaren's classic dark grey color","McLaren Argon","mclaren_mclaren_argon","626876"],
["McLaren_Mclaren_Orange","McLaren's classic orange color","Mclaren Orange","mclaren_mclaren_orange","FFC43D"],
["McLaren_Mercury_Red","McLaren's dark red color","Mercury Red","mclaren_mercury_red","9B0E1F"],
["McLaren_Pearl_White","McLaren's flat white color","Pearl White","mclaren_pearl_white","EBEBEB"],
["McLaren_Racing_Green","McLaren's British racing green color","Racing Green","mclaren_racing_green","2F473A"],
["McLaren_Sapphire_Black","McLaren's classic black color","Sapphire Black","mclaren_sapphire_black","29324E"],
["McLaren_Storm_Grey","McLaren's classic grey color","Storm Grey","mclaren_storm_grey","8C8D92"],
["McLaren_Titanium_Silver","McLaren's classic silver color","Titanium Silver","mclaren_titanium_silver","9BA2B4"],
["McLaren_Vegas_Blue","McLaren's classic blue color","Vegas Blue","mclaren_vegas_blue","0149D3"],
["McLaren_Volcano_Orange","McLaren's fire orange color","Volcano Orange","mclaren_volcano_orange","C82504"],
["McLaren_Volcano_Red","McLaren's fire red color","Volcano Red","mclaren_volcano_red","A80115"],
["Porsche_Acid_Green","Porsche's electric green color","Acid Green","porsche_acid_green","CBE800"],
["Porsche_Agate_Grey_Metallic","Porsche's metallic grey color","Agate Grey Metallic","porsche_agate_grey_metallic","AAB1B9"],
["Porsche_Arrow_Blue","Porsche's bright blue color","Arrow Blue","porsche_arrow_blue","0459DA"],
["Porsche_Aventurine_Green_Metallic","Porsche's metallic dark green color","Aventurine Green Metallic","porsche_aventurine_green_metallic","605E51"],
["Porsche_Azure_Blue","Porsche's classic blue color","Azure Blue","porsche_azure_blue","3C566F"],
["Porsche_Bahama_Blue","Porsche's bright metallic blue color","Bahama Blue","porsche_bahama_blue","2971EA"],
["Porsche_Carbon_Black_Metallic","Porsche's bright metallic black color","Carbon Black Metallic","porsche_carbon_black_metallic","74828B"],
["Porsche_Carmine_Red","Porsche's deep red color","Carmine Red","porsche_carmine_red","9D0620"],
["Porsche_Chalk","Porsche's light grey color","Chalk","porsche_chalk","A5A4AC"],
["Porsche_Dolomite_Silver_Metallic","Porsche's metallic silver color","Dolomite Silver Metallic","porsche_dolomite_silver_metallic","9FB1BC"],
["Porsche_Emerald_Green_Metalli","Porsche's British racing green color","Emerald Green Metalli","porsche_emerald_green_metalli","328983"],
["Porsche_Gentian_Blue_Metallic","Porsche's metallic blue color","Gentian Blue Metallic","porsche_gentian_blue_metallic","09203F"],
["Porsche_Graphite_Grey","Porsche's classic grey color","Graphite Grey","porsche_graphite_grey","748795"],
["Porsche_Graphite_Metallic","Porsche's bright grey color","Graphite Metallic","porsche_graphite_metallic","546A78"],
["Porsche_GT_Silver_Metallic","Porsche's light metallic grey color","GT Silver Metallic","porsche_gt_silver_metallic","A3ACB3"],
["Porsche_Guards_Red","Porsche's classic red color","Guards Red","porsche_guards_red","FA2223"],
["Porsche_Ice_Blue_Metallic","Porsche's light metallic blue color","Ice Blue Metallic","porsche_ice_blue_metallic","8C969F"],
["Porsche_Jade_Green","Porsche's bright teal color","Jade Green","porsche_jade_green","00BC96"],
["Porsche_Jet_Black_Metallic","Porsche's metallic black color","Jet Black Metallic","porsche_jet_black_metallic","201A1E"],
["Porsche_Lava_Orange","Porsche's classic orange color","Lava Orange","porsche_lava_orange","FF2600"],
["Porsche_Metallic_Blue","Porsche's classic metallic blue color","Metallic Blue","porsche_metallic_blue","0387D9"],
["Porsche_Miami_Blue","Porsche's light blue color","Miami Blue","porsche_miami_blue","00B5C8"],
["Porsche_Moonlight_Blue_Metallic","Porsche's dark metallic blue color","Moonlight Blue Metallic","porsche_moonlight_blue_metallic","153149"],
["Porsche_Night_Blue_Metallic","Porsche's dark metallic blue color","Night Blue Metallic","porsche_night_blue_metallic","385D89"],
["Porsche_Pastel_blue","Porsche's light pastel blue color","Pastel blue","porsche_pastel_blue","A0D8FB"],
["Porsche_Polo_Red","Porsche's classic red color","Polo Red","porsche_polo_red","980611"],
["Porsche_Python_Green","Porsche's bright green color","Python Green","porsche_python_green","1FF497"],
["Porsche_Racing_Yellow","Porsche's classic yellow color","Racing Yellow","porsche_racing_yellow","F8CD02"],
["Porsche_Red_Metallic","Porsche's metallic red color","Red Metallic","porsche_red_metallic","A72241"],
["Porsche_Riviera_Blue","Porsche's bright blue color","Riviera Blue","porsche_riviera_blue","018ADA"],
["Porsche_Rubystone_Red","Porsche's pink ruby color","Rubystone Red","porsche_rubystone_red","F3037E"],
["Porsche_Sand_Beige","Porsche's flat beige color","Sand Beige","porsche_sand_beige","C9AC80"],
["Porsche_Scarlet_Red","Porsche's red/orange color","Scarlet Red","porsche_scarlet_red","F82100"],
["Porsche_Viper_Green","Porsche's classic green color","Viper Green","porsche_viper_green","029220"]
]