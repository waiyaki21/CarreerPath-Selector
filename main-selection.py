import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap import ttk
import pandas as pd
import tkinter.font as tkFont

# Initialize main Tkinter window
root = tk.Tk()
fontFamily = {
    "default": "Arial",
    "alternate": "Century Gothic",
    "secondary": "Calibri"
} 
fontFamilies = {
    "default": fontFamily["default"],
    "headers": fontFamily["default"],
    "labels": fontFamily["alternate"],
    "buttons": fontFamily["default"],
    "text": fontFamily["alternate"],
    "table": fontFamily["secondary"],
    "menu": fontFamily["default"]
}
fontSize = {
    "small": 8,
    "medium": 10,
    "default": 11,
    "large": 12,
    "xlarge": 14
}

# === Sample Pathways and Tracks ===
pathway_tracks = {
    "STEM": ["PURE SCIENCES", "APPLIED SCIENCES", "TECHNICAL STUDIES"],
    "SOCIAL SCIENCES": ["LANGUAGES & LITERATURE", "HUMANITIES & BUSINESS STUDIES"],
    "ARTS & SPORTS": ["ARTS", "SPORTS & RECREATION"]
}

# === Placeholder for raw_data_map ===
raw_data_map = {
    "PURE SCIENCES": """
Biology,Building & Construction,Chemistry
Code: ST1044 | Track: PURE SCIENCES
Agriculture,Biology,Chemistry
Code: ST1042 | Track: PURE SCIENCES
Advanced Mathematics,Business Studies,General Science
Code: ST1026 | Track: PURE SCIENCES
Advanced Mathematics,Electricity,Physics
Code: ST1035 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Building & Construction
Code: ST1005 | Track: PURE SCIENCES
Advanced Mathematics,Metal Work,Physics
Code: ST1039 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Geography
Code: ST1016 | Track: PURE SCIENCES
Aviation,Biology,Chemistry
Code: ST1043 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Wood Work
Code: ST1022 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Power Mechanics
Code: ST1008 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Marine & Fisheries
Code: ST1018 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Electricity
Code: ST1015 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Physics
Code: ST1007 | Track: PURE SCIENCES
Advanced Mathematics,Aviation,General Science
Code: ST1024 | Track: PURE SCIENCES
Advanced Mathematics,Computer Studies,Physics
Code: ST1034 | Track: PURE SCIENCES
Advanced Mathematics,Agriculture,General Science
Code: ST1023 | Track: PURE SCIENCES
Advanced Mathematics,Business Studies,Physics
Code: ST1033 | Track: PURE SCIENCES
Advanced Mathematics,Agriculture,Chemistry
Code: ST1010 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Metal Work
Code: ST1006 | Track: PURE SCIENCES
Advanced Mathematics,Aviation,Chemistry
Code: ST1011 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Chemistry
Code: ST1004 | Track: PURE SCIENCES
Advanced Mathematics,Marine & Fisheries,Physics
Code: ST1038 | Track: PURE SCIENCES
Advanced Mathematics,Physics,Wood Work
Code: ST1041 | Track: PURE SCIENCES
Advanced Mathematics,Aviation,Physics
Code: ST1031 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Marine & Fisheries
Code: ST1047 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Wood Work
Code: ST1009 | Track: PURE SCIENCES
Advanced Mathematics,General Science,Geography
Code: ST1028 | Track: PURE SCIENCES
Advanced Mathematics,Agriculture,Physics
Code: ST1030 | Track: PURE SCIENCES
Biology,Business Studies,Chemistry
Code: ST1045 | Track: PURE SCIENCES
Advanced Mathematics,Building & Construction,Chemistry
Code: ST1012 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Computer Studies
Code: ST1014 | Track: PURE SCIENCES
Advanced Mathematics,Aviation,Biology
Code: ST1002 | Track: PURE SCIENCES
Advanced Mathematics,Agriculture,Biology
Code: ST1001 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Power Mechanics
Code: ST1021 | Track: PURE SCIENCES
Biology,Chemistry,Computer Studies
Code: ST1046 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Metal Work
Code: ST1019 | Track: PURE SCIENCES
Advanced Mathematics,Physics,Power Mechanics
Code: ST1040 | Track: PURE SCIENCES
Advanced Mathematics,Building & Construction,Physics
Code: ST1032 | Track: PURE SCIENCES
Advanced Mathematics,Business Studies,Chemistry
Code: ST1013 | Track: PURE SCIENCES
Advanced Mathematics,Geography,Physics
Code: ST1036 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Home Science
Code: ST1017 | Track: PURE SCIENCES
Advanced Mathematics,Home Science,Physics
Code: ST1037 | Track: PURE SCIENCES
Advanced Mathematics,General Science,Home Science
Code: ST1029 | Track: PURE SCIENCES
Advanced Mathematics,Computer Studies,General Science
Code: ST1027 | Track: PURE SCIENCES
Advanced Mathematics,Building & Construction,General Science
Code: ST1025 | Track: PURE SCIENCES
Advanced Mathematics,Chemistry,Physics
Code: ST1020 | Track: PURE SCIENCES
Advanced Mathematics,Biology,Business Studies
Code: ST1003 | Track: PURE SCIENCES
""",
    "APPLIED SCIENCES": """
Business Studies,Computer Studies,Physics
Code: ST2007 | Track: APPLIED SCIENCES
Agriculture,Building & Construction,Business Studies
Code: ST2045 | Track: APPLIED SCIENCES
Agriculture,Aviation,Geography
Code: ST2070 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Physics
Code: ST2067 | Track: APPLIED SCIENCES
Advanced Mathematics,Agriculture,Home Science
Code: ST2091 | Track: APPLIED SCIENCES
Agriculture,Geography,Physics
Code: ST2075 | Track: APPLIED SCIENCES
Computer Studies,Home Science,Wood Work
Code: ST2019 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Electricity
Code: ST2048 | Track: APPLIED SCIENCES
Agriculture,Business Studies,General Science
Code: ST2049 | Track: APPLIED SCIENCES
Agriculture,Building & Construction,Computer Studies
Code: ST2058 | Track: APPLIED SCIENCES
Biology,Business Studies,Computer Studies
Code: ST2097 | Track: APPLIED SCIENCES
Advanced Mathematics,Business Studies,Computer Studies
Code: ST2077 | Track: APPLIED SCIENCES
Advanced Mathematics,Biology,Geography
Code: ST2040 | Track: APPLIED SCIENCES
Agriculture,Aviation,Computer Studies
Code: ST2056 | Track: APPLIED SCIENCES
Aviation,Business Studies,Computer Studies
Code: ST2096 | Track: APPLIED SCIENCES
Agriculture,Chemistry,Computer Studies
Code: ST2059 | Track: APPLIED SCIENCES
Aviation,Computer Studies,Home Science
Code: ST2020 | Track: APPLIED SCIENCES
Agriculture,Home Science,Metal Work
Code: ST2092 | Track: APPLIED SCIENCES
Computer Studies,Geography,Metal Work
Code: ST2017 | Track: APPLIED SCIENCES
Agriculture,Building & Construction,Home Science
Code: ST2083 | Track: APPLIED SCIENCES
Agriculture,Home Science,Marine & Fisheries
Code: ST2090 | Track: APPLIED SCIENCES
Chemistry,Computer Studies,Home Science
Code: ST2024 | Track: APPLIED SCIENCES
Agriculture,Home Science,Wood Work
Code: ST2095 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Electricity
Code: ST2060 | Track: APPLIED SCIENCES
Business Studies,Computer Studies,Wood Work
Code: ST2009 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Computer Studies
Code: ST2047 | Track: APPLIED SCIENCES
Building & Construction,Business Studies,Computer Studies
Code: ST2098 | Track: APPLIED SCIENCES
Agriculture,Aviation,Business Studies
Code: ST2043 | Track: APPLIED SCIENCES
Computer Studies,Home Science,Marine & Fisheries
Code: ST2028 | Track: APPLIED SCIENCES
Agriculture,Geography,Wood Work
Code: ST2078 | Track: APPLIED SCIENCES
Aviation,Computer Studies,Geography
Code: ST2010 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Wood Work
Code: ST2055 | Track: APPLIED SCIENCES
Business Studies,Computer Studies,Electricity
Code: ST2001 | Track: APPLIED SCIENCES
Computer Studies,Electricity,Home Science
Code: ST2025 | Track: APPLIED SCIENCES
Agriculture,Home Science,Physics
Code: ST2093 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Wood Work
Code: ST2069 | Track: APPLIED SCIENCES
Agriculture,Geography,Power Mechanics
Code: ST2076 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Physics
Code: ST2053 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Home Science
Code: ST2063 | Track: APPLIED SCIENCES
Business Studies,Computer Studies,Marine & Fisheries
Code: ST2004 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Home Science
Code: ST2085 | Track: APPLIED SCIENCES
Computer Studies,Home Science,Metal Work
Code: ST2030 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Chemistry
Code: ST2046 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Marine & Fisheries
Code: ST2051 | Track: APPLIED SCIENCES
Agriculture,Electricity,Home Science
Code: ST2087 | Track: APPLIED SCIENCES
Computer Studies,Geography,Marine & Fisheries
Code: ST2015 | Track: APPLIED SCIENCES
Agriculture,Biology,Home Science
Code: ST2081 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Metal Work
Code: ST2066 | Track: APPLIED SCIENCES
Computer Studies,General Science,Geography
Code: ST2014 | Track: APPLIED SCIENCES
Biology,Computer Studies,Geography
Code: ST2011 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Metal Work
Code: ST2052 | Track: APPLIED SCIENCES
Agriculture,Chemistry,Home Science
Code: ST2086 | Track: APPLIED SCIENCES
Agriculture,Geography,Home Science
Code: ST2089 | Track: APPLIED SCIENCES
Advanced Mathematics,Agriculture,Computer Studies
Code: ST2065 | Track: APPLIED SCIENCES
Advanced Mathematics,Biology,Computer Studies
Code: ST2038 | Track: APPLIED SCIENCES
Computer Studies,Geography,Physics
Code: ST2018 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Marine & Fisheries
Code: ST2064 | Track: APPLIED SCIENCES
Agriculture,Biology,Geography
Code: ST2071 | Track: APPLIED SCIENCES
Building & Construction,Computer Studies,Geography
Code: ST2012 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Geography
Code: ST2062 | Track: APPLIED SCIENCES
Agriculture,Electricity,Geography
Code: ST2080 | Track: APPLIED SCIENCES
Advanced Mathematics,Biology,Electricity
Code: ST2039 | Track: APPLIED SCIENCES
Business Studies,Computer Studies,Home Science
Code: ST2023 | Track: APPLIED SCIENCES
Business Studies,Computer Studies,Metal Work
Code: ST2006 | Track: APPLIED SCIENCES
Agriculture,Home Science,Power Mechanics
Code: ST2094 | Track: APPLIED SCIENCES
Advanced Mathematics,Computer Studies,Geography
Code: ST2016 | Track: APPLIED SCIENCES
Computer Studies,Home Science,Physics
Code: ST2031 | Track: APPLIED SCIENCES
Chemistry,Computer Studies,Geography
Code: ST2013 | Track: APPLIED SCIENCES
Agriculture,Geography,Marine & Fisheries
Code: ST2084 | Track: APPLIED SCIENCES
Agriculture,General Science,Home Science
Code: ST2088 | Track: APPLIED SCIENCES
Business Studies,Computer Studies,General Science
Code: ST2002 | Track: APPLIED SCIENCES
Computer Studies,Home Science,Power Mechanics
Code: ST2032 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Power Mechanics
Code: ST2054 | Track: APPLIED SCIENCES
Agriculture,Aviation,Home Science
Code: ST2079 | Track: APPLIED SCIENCES
Agriculture,Biology,Business Studies
Code: ST2044 | Track: APPLIED SCIENCES
Business Studies,Computer Studies,Geography
Code: ST2003 | Track: APPLIED SCIENCES
Advanced Mathematics,Biology,Home Science
Code: ST2041 | Track: APPLIED SCIENCES
Agriculture,Biology,Computer Studies
Code: ST2057 | Track: APPLIED SCIENCES
Agriculture,General Science,Geography
Code: ST2082 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,Power Mechanics
Code: ST2068 | Track: APPLIED SCIENCES
Agriculture,Building & Construction,Geography
Code: ST2074 | Track: APPLIED SCIENCES
Agriculture,Geography,Metal Work
Code: ST2073 | Track: APPLIED SCIENCES
Agriculture,Business Studies,Geography
Code: ST2050 | Track: APPLIED SCIENCES
Agriculture,Computer Studies,General Science
Code: ST2061 | Track: APPLIED SCIENCES
Computer Studies,Geography,Home Science
Code: ST2027 | Track: APPLIED SCIENCES
Building & Construction,Computer Studies,Home Science
Code: ST2022 | Track: APPLIED SCIENCES
Advanced Mathematics,Agriculture,Geography
Code: ST2072 | Track: APPLIED SCIENCES
Business Studies,Chemistry,Computer Studies
Code: ST2099 | Track: APPLIED SCIENCES
Computer Studies,General Science,Home Science
Code: ST2026 | Track: APPLIED SCIENCES
""",
    "TECHNICAL STUDIES": """
General Science,Marine & Fisheries,Media Technology
Code: ST3050 | Track: TECHNICAL STUDIES
Aviation,Geography,Physics
Code: ST3121 | Track: TECHNICAL STUDIES
Computer Studies,General Science,Media Technology
Code: ST3074 | Track: TECHNICAL STUDIES
Biology,Business Studies,Metal Work
Code: ST3084 | Track: TECHNICAL STUDIES
Geography,Metal Work,Physics
Code: ST3105 | Track: TECHNICAL STUDIES
Biology,Geography,Power Mechanics
Code: ST3013 | Track: TECHNICAL STUDIES
Electricity,General Science,Home Science
Code: ST3008 | Track: TECHNICAL STUDIES
General Science,Marine & Fisheries,Power Mechanics
Code: ST3118 | Track: TECHNICAL STUDIES
Advanced Mathematics,General Science,Marine & Fisheries
Code: ST3047 | Track: TECHNICAL STUDIES
Chemistry,Geography,Power Mechanics
Code: ST3015 | Track: TECHNICAL STUDIES
Business Studies,Geography,Media Technology
Code: ST3068 | Track: TECHNICAL STUDIES
Biology,Business Studies,Media Technology
Code: ST3065 | Track: TECHNICAL STUDIES
Business Studies,Marine & Fisheries,Metal Work
Code: ST3089 | Track: TECHNICAL STUDIES
Aviation,Geography,Media Technology
Code: ST3120 | Track: TECHNICAL STUDIES
Business Studies,Media Technology,Metal Work
Code: ST3091 | Track: TECHNICAL STUDIES
General Science,Media Technology,Power Mechanics
Code: ST3011 | Track: TECHNICAL STUDIES
Computer Studies,General Science,Marine & Fisheries
Code: ST3044 | Track: TECHNICAL STUDIES
Advanced Mathematics,Electricity,Geography
Code: ST3024 | Track: TECHNICAL STUDIES
Chemistry,Geography,Marine & Fisheries
Code: ST3054 | Track: TECHNICAL STUDIES
Electricity,Geography,Marine & Fisheries
Code: ST3022 | Track: TECHNICAL STUDIES
General Science,Media Technology,Wood Work
Code: ST3053 | Track: TECHNICAL STUDIES
Computer Studies,Electricity,Geography
Code: ST3006 | Track: TECHNICAL STUDIES
Geography,Media Technology,Physics
Code: ST3082 | Track: TECHNICAL STUDIES
Business Studies,Physics,Wood Work
Code: ST3038 | Track: TECHNICAL STUDIES
Business Studies,Chemistry,Power Mechanics
Code: ST3107 | Track: TECHNICAL STUDIES
Advanced Mathematics,Geography,Media Technology
Code: ST3081 | Track: TECHNICAL STUDIES
Business Studies,Chemistry,Metal Work
Code: ST3085 | Track: TECHNICAL STUDIES
Geography,Home Science,Power Mechanics
Code: ST3018 | Track: TECHNICAL STUDIES
Business Studies,Home Science,Wood Work
Code: ST3034 | Track: TECHNICAL STUDIES
Advanced Mathematics,Geography,Metal Work
Code: ST3103 | Track: TECHNICAL STUDIES
Computer Studies,Geography,Media Technology
Code: ST3079 | Track: TECHNICAL STUDIES
Chemistry,Geography,Metal Work
Code: ST3099 | Track: TECHNICAL STUDIES
Chemistry,Electricity,Geography
Code: ST3017 | Track: TECHNICAL STUDIES
Geography,Home Science,Wood Work
Code: ST3060 | Track: TECHNICAL STUDIES
Biology,Electricity,Geography
Code: ST3014 | Track: TECHNICAL STUDIES
Business Studies,General Science,Metal Work
Code: ST3086 | Track: TECHNICAL STUDIES
Computer Studies,Geography,Power Mechanics
Code: ST3016 | Track: TECHNICAL STUDIES
Aviation,Business Studies,Metal Work
Code: ST3083 | Track: TECHNICAL STUDIES
General Science,Geography,Wood Work
Code: ST3046 | Track: TECHNICAL STUDIES
General Science,Media Technology,Metal Work
Code: ST3097 | Track: TECHNICAL STUDIES
Business Studies,Geography,Wood Work
Code: ST3032 | Track: TECHNICAL STUDIES
Geography,Marine & Fisheries,Media Technology
Code: ST3061 | Track: TECHNICAL STUDIES
Geography,Media Technology,Metal Work
Code: ST3104 | Track: TECHNICAL STUDIES
Biology,Business Studies,Wood Work
Code: ST3027 | Track: TECHNICAL STUDIES
Advanced Mathematics,General Science,Wood Work
Code: ST3051 | Track: TECHNICAL STUDIES
Business Studies,Marine & Fisheries,Wood Work
Code: ST3035 | Track: TECHNICAL STUDIES
Advanced Mathematics,Business Studies,Metal Work
Code: ST3090 | Track: TECHNICAL STUDIES
Advanced Mathematics,Business Studies,Marine & Fisheries
Code: ST3040 | Track: TECHNICAL STUDIES
Geography,Physics,Wood Work
Code: ST3071 | Track: TECHNICAL STUDIES
Advanced Mathematics,Geography,Marine & Fisheries
Code: ST3059 | Track: TECHNICAL STUDIES
Business Studies,Media Technology,Physics
Code: ST3073 | Track: TECHNICAL STUDIES
Business Studies,General Science,Wood Work
Code: ST3031 | Track: TECHNICAL STUDIES
Business Studies,Chemistry,Wood Work
Code: ST3029 | Track: TECHNICAL STUDIES
Geography,Marine & Fisheries,Physics
Code: ST3062 | Track: TECHNICAL STUDIES
Advanced Mathematics,Business Studies,Power Mechanics
Code: ST3113 | Track: TECHNICAL STUDIES
General Science,Marine & Fisheries,Metal Work
Code: ST3095 | Track: TECHNICAL STUDIES
Business Studies,Chemistry,Media Technology
Code: ST3066 | Track: TECHNICAL STUDIES
Advanced Mathematics,General Science,Metal Work
Code: ST3096 | Track: TECHNICAL STUDIES
Computer Studies,General Science,Wood Work
Code: ST3043 | Track: TECHNICAL STUDIES
Geography,Physics,Power Mechanics
Code: ST3023 | Track: TECHNICAL STUDIES
Chemistry,Geography,Media Technology
Code: ST3078 | Track: TECHNICAL STUDIES
Biology,Geography,Wood Work
Code: ST3055 | Track: TECHNICAL STUDIES
General Science,Home Science,Metal Work
Code: ST3094 | Track: TECHNICAL STUDIES
Business Studies,Computer Studies,Media Technology
Code: ST3067 | Track: TECHNICAL STUDIES
Advanced Mathematics,Geography,Power Mechanics
Code: ST3020 | Track: TECHNICAL STUDIES
Business Studies,Marine & Fisheries,Physics
Code: ST3042 | Track: TECHNICAL STUDIES
Business Studies,Physics,Power Mechanics
Code: ST3115 | Track: TECHNICAL STUDIES
General Science,Home Science,Power Mechanics
Code: ST3117 | Track: TECHNICAL STUDIES
Business Studies,Media Technology,Power Mechanics
Code: ST3114 | Track: TECHNICAL STUDIES
Business Studies,Geography,Power Mechanics
Code: ST3110 | Track: TECHNICAL STUDIES
Geography,Marine & Fisheries,Wood Work
Code: ST3063 | Track: TECHNICAL STUDIES
Business Studies,General Science,Marine & Fisheries
Code: ST3033 | Track: TECHNICAL STUDIES
Advanced Mathematics,Electricity,General Science
Code: ST3010 | Track: TECHNICAL STUDIES
Electricity,Geography,Physics
Code: ST3026 | Track: TECHNICAL STUDIES
Business Studies,General Science,Power Mechanics
Code: ST3109 | Track: TECHNICAL STUDIES
General Science,Home Science,Marine & Fisheries
Code: ST3045 | Track: TECHNICAL STUDIES
General Science,Home Science,Media Technology
Code: ST3075 | Track: TECHNICAL STUDIES
Biology,Business Studies,Power Mechanics
Code: ST3106 | Track: TECHNICAL STUDIES
Geography,Home Science,Metal Work
Code: ST3101 | Track: TECHNICAL STUDIES
Electricity,Geography,Home Science
Code: ST3007 | Track: TECHNICAL STUDIES
Chemistry,Geography,Wood Work
Code: ST3056 | Track: TECHNICAL STUDIES
Electricity,General Science,Marine & Fisheries
Code: ST3009 | Track: TECHNICAL STUDIES
Geography,Home Science,Media Technology
Code: ST3080 | Track: TECHNICAL STUDIES
Computer Studies,Geography,Wood Work
Code: ST3057 | Track: TECHNICAL STUDIES
Business Studies,Marine & Fisheries,Power Mechanics
Code: ST3112 | Track: TECHNICAL STUDIES
Geography,Media Technology,Power Mechanics
Code: ST3021 | Track: TECHNICAL STUDIES
Geography,Home Science,Marine & Fisheries
Code: ST3058 | Track: TECHNICAL STUDIES
Business Studies,Computer Studies,Power Mechanics
Code: ST3108 | Track: TECHNICAL STUDIES
General Science,Home Science,Wood Work
Code: ST3048 | Track: TECHNICAL STUDIES
Advanced Mathematics,Geography,Wood Work
Code: ST3064 | Track: TECHNICAL STUDIES
Geography,Marine & Fisheries,Power Mechanics
Code: ST3019 | Track: TECHNICAL STUDIES
Biology,Geography,Metal Work
Code: ST3098 | Track: TECHNICAL STUDIES
General Science,Marine & Fisheries,Wood Work
Code: ST3049 | Track: TECHNICAL STUDIES
Business Studies,Metal Work,Physics
Code: ST3092 | Track: TECHNICAL STUDIES
Electricity,Geography,Media Technology
Code: ST3025 | Track: TECHNICAL STUDIES
Business Studies,Geography,Metal Work
Code: ST3087 | Track: TECHNICAL STUDIES
Business Studies,Home Science,Metal Work
Code: ST3088 | Track: TECHNICAL STUDIES
Business Studies,Marine & Fisheries,Media Technology
Code: ST3041 | Track: TECHNICAL STUDIES
Geography,Marine & Fisheries,Metal Work
Code: ST3102 | Track: TECHNICAL STUDIES
Advanced Mathematics,Business Studies,Media Technology
Code: ST3072 | Track: TECHNICAL STUDIES
General Science,Geography,Metal Work
Code: ST3100 | Track: TECHNICAL STUDIES
Business Studies,Geography,Marine & Fisheries
Code: ST3037 | Track: TECHNICAL STUDIES
Business Studies,Chemistry,Marine & Fisheries
Code: ST3030 | Track: TECHNICAL STUDIES
Advanced Mathematics,General Science,Media Technology
Code: ST3076 | Track: TECHNICAL STUDIES
Biology,Geography,Media Technology
Code: ST3077 | Track: TECHNICAL STUDIES
Advanced Mathematics,Business Studies,Wood Work
Code: ST3036 | Track: TECHNICAL STUDIES
Business Studies,Home Science,Marine & Fisheries
Code: ST3039 | Track: TECHNICAL STUDIES
Advanced Mathematics,General Science,Power Mechanics
Code: ST3119 | Track: TECHNICAL STUDIES
Business Studies,Home Science,Power Mechanics
Code: ST3111 | Track: TECHNICAL STUDIES
Geography,Media Technology,Wood Work
Code: ST3069 | Track: TECHNICAL STUDIES
Computer Studies,General Science,Power Mechanics
Code: ST3116 | Track: TECHNICAL STUDIES
Electricity,General Science,Media Technology
Code: ST3012 | Track: TECHNICAL STUDIES
Business Studies,Home Science,Media Technology
Code: ST3070 | Track: TECHNICAL STUDIES
Computer Studies,General Science,Metal Work
Code: ST3093 | Track: TECHNICAL STUDIES
Biology,Business Studies,Marine & Fisheries
Code: ST3028 | Track: TECHNICAL STUDIES
Biology,Geography,Marine & Fisheries
Code: ST3052 | Track: TECHNICAL STUDIES
""",
    "LANGUAGES & LITERATURE": """
Arabic,Computer Studies,French
Code: SS1006 | Track: LANGUAGES & LITERATURE
Computer Studies,Fasihi ya Kiswahili,Indigenous Language
Code: SS1040 | Track: LANGUAGES & LITERATURE
General Science,Indigenous Language,Literature in English
Code: SS1060 | Track: LANGUAGES & LITERATURE
Arabic,Christian Religious Education,Kenya Sign Language
Code: SS1059 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,General Science,Kenya Sign Language
Code: SS1037 | Track: LANGUAGES & LITERATURE
Advanced Mathematics,French,Mandarine Chinese
Code: SS1084 | Track: LANGUAGES & LITERATURE
Advanced Mathematics,Fasihi ya Kiswahili,Kenya Sign Language
Code: SS1044 | Track: LANGUAGES & LITERATURE
Arabic,French,General Science
Code: SS1014 | Track: LANGUAGES & LITERATURE
German,Indigenous Language,Literature in English
Code: SS1065 | Track: LANGUAGES & LITERATURE
French,Indigenous Language,Literature in English
Code: SS1001 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Indigenous Language,Literature in English
Code: SS1002 | Track: LANGUAGES & LITERATURE
Arabic,Computer Studies,Kenya Sign Language
Code: SS1058 | Track: LANGUAGES & LITERATURE
Arabic,Fasihi ya Kiswahili,Indigenous Language
Code: SS1043 | Track: LANGUAGES & LITERATURE
Arabic,French,Hindu Religious Education
Code: SS1011 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Indigenous Language,Kenya Sign Language
Code: SS1018 | Track: LANGUAGES & LITERATURE
Advanced Mathematics,Arabic,French
Code: SS1019 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,General Science,Indigenous Language
Code: SS1029 | Track: LANGUAGES & LITERATURE
French,German,Islamic Religious Education
Code: SS1050 | Track: LANGUAGES & LITERATURE
Arabic,French,Kenya Sign Language
Code: SS1064 | Track: LANGUAGES & LITERATURE
Advanced Mathematics,Arabic,Kenya Sign Language
Code: SS1074 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Hindu Religious Education,Kenya Sign Language
Code: SS1033 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,German,Indigenous Language
Code: SS1025 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Hindu Religious Education,Indigenous Language
Code: SS1036 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Indigenous Language,Mandarine Chinese
Code: SS1022 | Track: LANGUAGES & LITERATURE
Advanced Mathematics,Fasihi ya Kiswahili,Indigenous Language
Code: SS1020 | Track: LANGUAGES & LITERATURE
French,Geography,Mandarine Chinese
Code: SS1055 | Track: LANGUAGES & LITERATURE
Indigenous Language,Islamic Religious Education,Literature in English
Code: SS1007 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Kenya Sign Language,Mandarine Chinese
Code: SS1026 | Track: LANGUAGES & LITERATURE
Advanced Mathematics,Indigenous Language,Literature in English
Code: SS1069 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Islamic Religious Education,Kenya Sign Language
Code: SS1031 | Track: LANGUAGES & LITERATURE
Christian Religious Education,French,Mandarine Chinese
Code: SS1077 | Track: LANGUAGES & LITERATURE
Arabic,Business Studies,Kenya Sign Language
Code: SS1057 | Track: LANGUAGES & LITERATURE
Advanced Mathematics,French,German
Code: SS1046 | Track: LANGUAGES & LITERATURE
Business Studies,Fasihi ya Kiswahili,Kenya Sign Language
Code: SS1023 | Track: LANGUAGES & LITERATURE
Business Studies,Fasihi ya Kiswahili,Literature in English
Code: SS1080 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Indigenous Language,Islamic Religious Education
Code: SS1038 | Track: LANGUAGES & LITERATURE
French,Geography,German
Code: SS1051 | Track: LANGUAGES & LITERATURE
Christian Religious Education,Fasihi ya Kiswahili,Kenya Sign Language
Code: SS1030 | Track: LANGUAGES & LITERATURE
Indigenous Language,Literature in English,Mandarine Chinese
Code: SS1068 | Track: LANGUAGES & LITERATURE
Arabic,Geography,Kenya Sign Language
Code: SS1070 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,History & Citizenship,Kenya Sign Language
Code: SS1041 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Geography,Kenya Sign Language
Code: SS1039 | Track: LANGUAGES & LITERATURE
French,Hindu Religious Education,Mandarine Chinese
Code: SS1079 | Track: LANGUAGES & LITERATURE
French,German,History & Citizenship
Code: SS1049 | Track: LANGUAGES & LITERATURE
Computer Studies,French,German
Code: SS1047 | Track: LANGUAGES & LITERATURE
History & Citizenship,Indigenous Language,Literature in English
Code: SS1067 | Track: LANGUAGES & LITERATURE
Arabic,French,Islamic Religious Education
Code: SS1009 | Track: LANGUAGES & LITERATURE
French,Islamic Religious Education,Mandarine Chinese
Code: SS1078 | Track: LANGUAGES & LITERATURE
Christian Religious Education,Fasihi ya Kiswahili,Indigenous Language
Code: SS1034 | Track: LANGUAGES & LITERATURE
Indigenous Language,Kenya Sign Language,Literature in English
Code: SS1071 | Track: LANGUAGES & LITERATURE
Arabic,French,Mandarine Chinese
Code: SS1017 | Track: LANGUAGES & LITERATURE
Business Studies,French,Mandarine Chinese
Code: SS1075 | Track: LANGUAGES & LITERATURE
French,German,Hindu Religious Education
Code: SS1052 | Track: LANGUAGES & LITERATURE
Arabic,French,History & Citizenship
Code: SS1016 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,French,Indigenous Language
Code: SS1032 | Track: LANGUAGES & LITERATURE
Hindu Religious Education,Indigenous Language,Literature in English
Code: SS1005 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Literature in English,Mandarine Chinese
Code: SS1082 | Track: LANGUAGES & LITERATURE
Arabic,Islamic Religious Education,Kenya Sign Language
Code: SS1062 | Track: LANGUAGES & LITERATURE
Computer Studies,French,Mandarine Chinese
Code: SS1076 | Track: LANGUAGES & LITERATURE
Arabic,General Science,Kenya Sign Language
Code: SS1066 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Kenya Sign Language,Literature in English
Code: SS1083 | Track: LANGUAGES & LITERATURE
Business Studies,French,German
Code: SS1045 | Track: LANGUAGES & LITERATURE
Business Studies,Fasihi ya Kiswahili,Indigenous Language
Code: SS1042 | Track: LANGUAGES & LITERATURE
Computer Studies,Fasihi ya Kiswahili,Kenya Sign Language
Code: SS1028 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,History & Citizenship,Indigenous Language
Code: SS1024 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,History & Citizenship,Literature in English
Code: SS1081 | Track: LANGUAGES & LITERATURE
French,History & Citizenship,Mandarine Chinese
Code: SS1056 | Track: LANGUAGES & LITERATURE
Arabic,History & Citizenship,Kenya Sign Language
Code: SS1072 | Track: LANGUAGES & LITERATURE
Arabic,Business Studies,French
Code: SS1004 | Track: LANGUAGES & LITERATURE
Geography,Indigenous Language,Literature in English
Code: SS1061 | Track: LANGUAGES & LITERATURE
Arabic,French,Geography
Code: SS1015 | Track: LANGUAGES & LITERATURE
French,General Science,Mandarine Chinese
Code: SS1054 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,French,Kenya Sign Language
Code: SS1035 | Track: LANGUAGES & LITERATURE
Arabic,Fasihi ya Kiswahili,Kenya Sign Language
Code: SS1021 | Track: LANGUAGES & LITERATURE
Business Studies,Indigenous Language,Literature in English
Code: SS1012 | Track: LANGUAGES & LITERATURE
Arabic,Hindu Religious Education,Kenya Sign Language
Code: SS1063 | Track: LANGUAGES & LITERATURE
French,General Science,German
Code: SS1053 | Track: LANGUAGES & LITERATURE
Computer Studies,Indigenous Language,Literature in English
Code: SS1010 | Track: LANGUAGES & LITERATURE
Christian Religious Education,French,German
Code: SS1048 | Track: LANGUAGES & LITERATURE
Fasihi ya Kiswahili,Geography,Indigenous Language
Code: SS1027 | Track: LANGUAGES & LITERATURE
Christian Religious Education,Indigenous Language,Literature in English
Code: SS1003 | Track: LANGUAGES & LITERATURE
Arabic,Kenya Sign Language,Mandarine Chinese
Code: SS1073 | Track: LANGUAGES & LITERATURE
Arabic,Indigenous Language,Literature in English
Code: SS1013 | Track: LANGUAGES & LITERATURE
Arabic,Christian Religious Education,French
Code: SS1008 | Track: LANGUAGES & LITERATURE
""",
    "HUMANITIES & BUSINESS STUDIES": """
Computer Studies,Geography,Islamic Religious Education
Code: SS2033 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Geography,Mandarine Chinese
Code: SS2050 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Geography,History & Citizenship
Code: SS2019 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,French
Code: SS2112 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Geography,Hindu Religious Education
Code: SS2055 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,German,History & Citizenship
Code: SS2099 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Geography,Literature in English
Code: SS2061 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Geography,Kenya Sign Language
Code: SS2118 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,German,Hindu Religious Education
Code: SS2002 | Track: HUMANITIES & BUSINESS STUDIES
General Science,Geography,Hindu Religious Education
Code: SS2041 | Track: HUMANITIES & BUSINESS STUDIES
Computer Studies,Geography,History & Citizenship
Code: SS2024 | Track: HUMANITIES & BUSINESS STUDIES
Geography,History & Citizenship,Mandarine Chinese
Code: SS2092 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Christian Religious Education,History & Citizenship
Code: SS2057 | Track: HUMANITIES & BUSINESS STUDIES
Geography,History & Citizenship,Literature in English
Code: SS2004 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Geography,Indigenous Language
Code: SS2065 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Business Studies,Geography
Code: SS2056 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,German,Islamic Religious Education
Code: SS2003 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,History & Citizenship,Literature in English
Code: SS2100 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Hindu Religious Education,History & Citizenship
Code: SS2091 | Track: HUMANITIES & BUSINESS STUDIES
General Science,Geography,Islamic Religious Education
Code: SS2042 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Fasihi ya Kiswahili,Islamic Religious Education
Code: SS2110 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,General Science
Code: SS2115 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,History & Citizenship,Mandarine Chinese
Code: SS2101 | Track: HUMANITIES & BUSINESS STUDIES
Fasihi ya Kiswahili,Hindu Religious Education,History & Citizenship
Code: SS2071 | Track: HUMANITIES & BUSINESS STUDIES
General Science,Geography,History & Citizenship
Code: SS2013 | Track: HUMANITIES & BUSINESS STUDIES
Geography,German,Hindu Religious Education
Code: SS2044 | Track: HUMANITIES & BUSINESS STUDIES
French,Geography,Islamic Religious Education
Code: SS2039 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Fasihi ya Kiswahili,History & Citizenship
Code: SS2069 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Computer Studies,History & Citizenship
Code: SS2064 | Track: HUMANITIES & BUSINESS STUDIES
Hindu Religious Education,History & Citizenship,Mandarine Chinese
Code: SS2086 | Track: HUMANITIES & BUSINESS STUDIES
Fasihi ya Kiswahili,Geography,History & Citizenship
Code: SS2018 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,Fasihi ya Kiswahili
Code: SS2109 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Business Studies,Christian Religious Education
Code: SS2103 | Track: HUMANITIES & BUSINESS STUDIES
General Science,History & Citizenship,Islamic Religious Education
Code: SS2077 | Track: HUMANITIES & BUSINESS STUDIES
German,History & Citizenship,Islamic Religious Education
Code: SS2080 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Fasihi ya Kiswahili,Geography
Code: SS2035 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Business Studies,History & Citizenship
Code: SS2094 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Geography,History & Citizenship
Code: SS2026 | Track: HUMANITIES & BUSINESS STUDIES
History & Citizenship,Islamic Religious Education,Mandarine Chinese
Code: SS2087 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,French,History & Citizenship
Code: SS2097 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Business Studies,Hindu Religious Education
Code: SS2027 | Track: HUMANITIES & BUSINESS STUDIES
History & Citizenship,Islamic Religious Education,Literature in English
Code: SS2083 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,General Science,Islamic Religious Education
Code: SS2116 | Track: HUMANITIES & BUSINESS STUDIES
Computer Studies,Hindu Religious Education,History & Citizenship
Code: SS2062 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,German
Code: SS2005 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Hindu Religious Education,Literature in English
Code: SS2012 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,General Science,Hindu Religious Education
Code: SS2117 | Track: HUMANITIES & BUSINESS STUDIES
Geography,Hindu Religious Education,Mandarine Chinese
Code: SS2052 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,General Science,History & Citizenship
Code: SS2098 | Track: HUMANITIES & BUSINESS STUDIES
Geography,German,History & Citizenship
Code: SS2010 | Track: HUMANITIES & BUSINESS STUDIES
French,History & Citizenship,Islamic Religious Education
Code: SS2074 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Christian Religious Education,Geography
Code: SS2029 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Geography,Literature in English
Code: SS2047 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Geography,History & Citizenship
Code: SS2025 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Business Studies,Hindu Religious Education
Code: SS2105 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Geography,Hindu Religious Education
Code: SS2031 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Hindu Religious Education,History & Citizenship
Code: SS2006 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,Mandarine Chinese
Code: SS2017 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,General Science,History & Citizenship
Code: SS2076 | Track: HUMANITIES & BUSINESS STUDIES
Hindu Religious Education,History & Citizenship,Literature in English
Code: SS2085 | Track: HUMANITIES & BUSINESS STUDIES
Fasihi ya Kiswahili,History & Citizenship,Islamic Religious Education
Code: SS2070 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,German,History & Citizenship
Code: SS2079 | Track: HUMANITIES & BUSINESS STUDIES
Computer Studies,Geography,Hindu Religious Education
Code: SS2032 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Christian Religious Education,History & Citizenship
Code: SS2089 | Track: HUMANITIES & BUSINESS STUDIES
Computer Studies,History & Citizenship,Islamic Religious Education
Code: SS2063 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Geography,History & Citizenship
Code: SS2093 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,History & Citizenship
Code: SS2008 | Track: HUMANITIES & BUSINESS STUDIES
French,Geography,Hindu Religious Education
Code: SS2038 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,Literature in English
Code: SS2009 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Computer Studies,History & Citizenship
Code: SS2095 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,Computer Studies
Code: SS2106 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Geography,German
Code: SS2046 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,History & Citizenship,Islamic Religious Education
Code: SS2090 | Track: HUMANITIES & BUSINESS STUDIES
Geography,Islamic Religious Education,Mandarine Chinese
Code: SS2051 | Track: HUMANITIES & BUSINESS STUDIES
Geography,Islamic Religious Education,Literature in English
Code: SS2048 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Geography,Islamic Religious Education
Code: SS2054 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,Computer Studies,Geography
Code: SS2034 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Business Studies,Christian Religious Education
Code: SS2021 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,History & Citizenship,Mandarine Chinese
Code: SS2088 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Business Studies,Islamic Religious Education
Code: SS2023 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Computer Studies,Hindu Religious Education
Code: SS2108 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,History & Citizenship,Islamic Religious Education
Code: SS2058 | Track: HUMANITIES & BUSINESS STUDIES
Geography,Hindu Religious Education,Literature in English
Code: SS2049 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,History & Citizenship,Literature in English
Code: SS2082 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,French,Islamic Religious Education
Code: SS2113 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,French,Geography
Code: SS2068 | Track: HUMANITIES & BUSINESS STUDIES
German,Hindu Religious Education,History & Citizenship
Code: SS2081 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Hindu Religious Education,History & Citizenship
Code: SS2059 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Hindu Religious Education,Mandarine Chinese
Code: SS2014 | Track: HUMANITIES & BUSINESS STUDIES
Fasihi ya Kiswahili,Geography,Hindu Religious Education
Code: SS2037 | Track: HUMANITIES & BUSINESS STUDIES
Geography,Hindu Religious Education,History & Citizenship
Code: SS2020 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Business Studies,Islamic Religious Education
Code: SS2104 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Geography,Islamic Religious Education
Code: SS2030 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Geography,German
Code: SS2066 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Islamic Religious Education,Mandarine Chinese
Code: SS2015 | Track: HUMANITIES & BUSINESS STUDIES
Arabic,Business Studies,Geography
Code: SS2084 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Islamic Religious Education,Literature in English
Code: SS2011 | Track: HUMANITIES & BUSINESS STUDIES
Geography,History & Citizenship,Islamic Religious Education
Code: SS2022 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,French,Geography
Code: SS2040 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,General Science,Geography
Code: SS2067 | Track: HUMANITIES & BUSINESS STUDIES
French,Geography,History & Citizenship
Code: SS2016 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Fasihi ya Kiswahili,Hindu Religious Education
Code: SS2111 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Fasihi ya Kiswahili,Geography
Code: SS2073 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,French,Hindu Religious Education
Code: SS2114 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Business Studies,History & Citizenship
Code: SS2102 | Track: HUMANITIES & BUSINESS STUDIES
General Science,Hindu Religious Education,History & Citizenship
Code: SS2078 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,History & Citizenship,Islamic Religious Education
Code: SS2007 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Computer Studies,Islamic Religious Education
Code: SS2107 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,General Science,Geography
Code: SS2043 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Fasihi ya Kiswahili,History & Citizenship
Code: SS2096 | Track: HUMANITIES & BUSINESS STUDIES
Advanced Mathematics,Christian Religious Education,Geography
Code: SS2053 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Geography,Mandarine Chinese
Code: SS2060 | Track: HUMANITIES & BUSINESS STUDIES
Business Studies,Christian Religious Education,Geography
Code: SS2001 | Track: HUMANITIES & BUSINESS STUDIES
Geography,German,Islamic Religious Education
Code: SS2045 | Track: HUMANITIES & BUSINESS STUDIES
French,Hindu Religious Education,History & Citizenship
Code: SS2072 | Track: HUMANITIES & BUSINESS STUDIES
Fasihi ya Kiswahili,Geography,Islamic Religious Education
Code: SS2036 | Track: HUMANITIES & BUSINESS STUDIES
Christian Religious Education,French,History & Citizenship
Code: SS2075 | Track: HUMANITIES & BUSINESS STUDIES
""",
    "ARTS": """
Computer Studies,Fine Arts,Music & Dance
Code: AS1021 | Track: ARTS
Literature in English,Music & Dance,Theatre & Film
Code: AS1049 | Track: ARTS
Fine Arts,General Science,Music & Dance
Code: AS1027 | Track: ARTS
Business Studies,Music & Dance,Theatre & Film
Code: AS1038 | Track: ARTS
Fine Arts,Hindu Religious Education,Theatre & Film
Code: AS1007 | Track: ARTS
Hindu Religious Education,Music & Dance,Theatre & Film
Code: AS1042 | Track: ARTS
Biology,Fine Arts,Theatre & Film
Code: AS1002 | Track: ARTS
Arabic,Music & Dance,Theatre & Film
Code: AS1036 | Track: ARTS
Christian Religious Education,Fine Arts,Theatre & Film
Code: AS1005 | Track: ARTS
History & Citizenship,Music & Dance,Theatre & Film
Code: AS1048 | Track: ARTS
Arabic,Fine Arts,Theatre & Film
Code: AS1001 | Track: ARTS
Fine Arts,German,Theatre & Film
Code: AS1012 | Track: ARTS
Fasihi ya Kiswahili,Music & Dance,Theatre & Film
Code: AS1043 | Track: ARTS
Fine Arts,Mandarine Chinese,Music & Dance
Code: AS1032 | Track: ARTS
French,Music & Dance,Theatre & Film
Code: AS1044 | Track: ARTS
Fine Arts,German,Music & Dance
Code: AS1029 | Track: ARTS
Fine Arts,French,Theatre & Film
Code: AS1009 | Track: ARTS
Christian Religious Education,Fine Arts,Music & Dance
Code: AS1022 | Track: ARTS
Biology,Fine Arts,Music & Dance
Code: AS1019 | Track: ARTS
Fine Arts,Geography,Theatre & Film
Code: AS1011 | Track: ARTS
Fine Arts,History & Citizenship,Music & Dance
Code: AS1030 | Track: ARTS
Computer Studies,Music & Dance,Theatre & Film
Code: AS1039 | Track: ARTS
Arabic,Fine Arts,Music & Dance
Code: AS1018 | Track: ARTS
Fine Arts,Islamic Religious Education,Music & Dance
Code: AS1023 | Track: ARTS
Biology,Music & Dance,Theatre & Film
Code: AS1037 | Track: ARTS
German,Music & Dance,Theatre & Film
Code: AS1047 | Track: ARTS
Christian Religious Education,Music & Dance,Theatre & Film
Code: AS1040 | Track: ARTS
Fine Arts,Hindu Religious Education,Music & Dance
Code: AS1024 | Track: ARTS
Mandarine Chinese,Music & Dance,Theatre & Film
Code: AS1050 | Track: ARTS
Fine Arts,Mandarine Chinese,Theatre & Film
Code: AS1015 | Track: ARTS
Fine Arts,French,Music & Dance
Code: AS1026 | Track: ARTS
General Science,Music & Dance,Theatre & Film
Code: AS1045 | Track: ARTS
Business Studies,Fine Arts,Theatre & Film
Code: AS1003 | Track: ARTS
Advanced Mathematics,Fine Arts,Theatre & Film
Code: AS1016 | Track: ARTS
Fine Arts,Sports & Recreation,Theatre & Film
Code: AS1017 | Track: ARTS
Fine Arts,General Science,Theatre & Film
Code: AS1010 | Track: ARTS
Geography,Music & Dance,Theatre & Film
Code: AS1046 | Track: ARTS
Fine Arts,Geography,Music & Dance
Code: AS1028 | Track: ARTS
Advanced Mathematics,Music & Dance,Theatre & Film
Code: AS1051 | Track: ARTS
Music & Dance,Sports & Recreation,Theatre & Film
Code: AS1052 | Track: ARTS
Fasihi ya Kiswahili,Fine Arts,Theatre & Film
Code: AS1008 | Track: ARTS
Business Studies,Fine Arts,Music & Dance
Code: AS1020 | Track: ARTS
Computer Studies,Fine Arts,Theatre & Film
Code: AS1004 | Track: ARTS
Fine Arts,Literature in English,Theatre & Film
Code: AS1014 | Track: ARTS
Islamic Religious Education,Music & Dance,Theatre & Film
Code: AS1041 | Track: ARTS
Fine Arts,History & Citizenship,Theatre & Film
Code: AS1013 | Track: ARTS
Fine Arts,Music & Dance,Sports & Recreation
Code: AS1034 | Track: ARTS
Fine Arts,Music & Dance,Theatre & Film
Code: AS1035 | Track: ARTS
Fine Arts,Islamic Religious Education,Theatre & Film
Code: AS1006 | Track: ARTS
Fasihi ya Kiswahili,Fine Arts,Music & Dance
Code: AS1025 | Track: ARTS
Fine Arts,Literature in English,Music & Dance
Code: AS1031 | Track: ARTS
Advanced Mathematics,Fine Arts,Music & Dance
Code: AS1033 | Track: ARTS
""",
    "SPORTS & RECREATION": """
Biology,Geography,Sports & Recreation
Code: AS2009 | Track: SPORTS & RECREATION
Biology,Islamic Religious Education,Sports & Recreation
Code: AS2006 | Track: SPORTS & RECREATION
Biology,History & Citizenship,Sports & Recreation
Code: AS2011 | Track: SPORTS & RECREATION
General Science,Literature in English,Sports & Recreation
Code: AS2027 | Track: SPORTS & RECREATION
General Science,History & Citizenship,Sports & Recreation
Code: AS2026 | Track: SPORTS & RECREATION
Biology,Mandarine Chinese,Sports & Recreation
Code: AS2013 | Track: SPORTS & RECREATION
Advanced Mathematics,General Science,Sports & Recreation
Code: AS2029 | Track: SPORTS & RECREATION
Biology,Computer Studies,Sports & Recreation
Code: AS2003 | Track: SPORTS & RECREATION
General Science,Hindu Religious Education,Sports & Recreation
Code: AS2021 | Track: SPORTS & RECREATION
Arabic,Biology,Sports & Recreation
Code: AS2001 | Track: SPORTS & RECREATION
General Science,Media Technology,Sports & Recreation
Code: AS2030 | Track: SPORTS & RECREATION
Biology,Hindu Religious Education,Sports & Recreation
Code: AS2005 | Track: SPORTS & RECREATION
General Science,Islamic Religious Education,Sports & Recreation
Code: AS2020 | Track: SPORTS & RECREATION
Advanced Mathematics,Biology,Sports & Recreation
Code: AS2014 | Track: SPORTS & RECREATION
Business Studies,General Science,Sports & Recreation
Code: AS2017 | Track: SPORTS & RECREATION
Biology,Business Studies,Sports & Recreation
Code: AS2002 | Track: SPORTS & RECREATION
General Science,Geography,Sports & Recreation
Code: AS2024 | Track: SPORTS & RECREATION
Computer Studies,General Science,Sports & Recreation
Code: AS2018 | Track: SPORTS & RECREATION
General Science,Mandarine Chinese,Sports & Recreation
Code: AS2028 | Track: SPORTS & RECREATION
Biology,Fasihi ya Kiswahili,Sports & Recreation
Code: AS2007 | Track: SPORTS & RECREATION
Biology,Literature in English,Sports & Recreation
Code: AS2012 | Track: SPORTS & RECREATION
General Science,German,Sports & Recreation
Code: AS2025 | Track: SPORTS & RECREATION
Biology,German,Sports & Recreation
Code: AS2010 | Track: SPORTS & RECREATION
Biology,French,Sports & Recreation
Code: AS2008 | Track: SPORTS & RECREATION
Biology,Media Technology,Sports & Recreation
Code: AS2015 | Track: SPORTS & RECREATION
Christian Religious Education,General Science,Sports & Recreation
Code: AS2019 | Track: SPORTS & RECREATION
Biology,Christian Religious Education,Sports & Recreation
Code: AS2004 | Track: SPORTS & RECREATION
Fasihi ya Kiswahili,General Science,Sports & Recreation
Code: AS2022 | Track: SPORTS & RECREATION
French,General Science,Sports & Recreation
Code: AS2023 | Track: SPORTS & RECREATION
Arabic,General Science,Sports & Recreation
Code: AS2016 | Track: SPORTS & RECREATION
""",
}

# === Data Processing Function ===
def process_raw_data(pathway, track, filter_keywords=None):
    results = []
    all_tracks = []

    if pathway == "ALL":
        for pth, tr_list in pathway_tracks.items():
            for tr in tr_list:
                all_tracks.append((pth, tr))
    elif track == "ALL":
        for tr in pathway_tracks.get(pathway, []):
            all_tracks.append((pathway, tr))
    else:
        all_tracks.append((pathway, track))

    for pth, tr in all_tracks:
        raw_data = raw_data_map.get(tr.upper())
        if not raw_data:
            continue

        lines = [line.strip() for line in raw_data.strip().split('\n') if line.strip()]
        for i in range(0, len(lines), 2):
            subjects_raw = lines[i]
            code_line = lines[i + 1]

            code = code_line.split('|')[0].replace("Code:", "").strip()
            real_track = code_line.split('|')[1].replace("Track:", "").strip()
            subjects_split = [s.strip() for s in subjects_raw.split(',')]

            while len(subjects_split) < 3:
                subjects_split.append("")

            combined_subjects = [s.lower() for s in subjects_split]

            if filter_keywords:
                if not all(any(keyword in subject for subject in combined_subjects) for keyword in filter_keywords):
                    continue

            results.append({
                "NO": len(results) + 1,
                "CODE": code,
                "PATHWAY": pth.upper(),
                "TRACK": real_track.upper(),
                "SUBJECT 1": subjects_split[0],
                "SUBJECT 2": subjects_split[1],
                "SUBJECT 3": subjects_split[2],
            })

    return results

def auto_size_columns(tree):
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(family=fontFamilies["table"], size=fontSize["medium"])

    for col in tree["columns"]:
        max_width = default_font.measure(col)

        for item in tree.get_children():
            cell_value = tree.set(item, col)
            max_width = max(max_width, default_font.measure(cell_value))

        tree.column(col, width=max_width, minwidth=50)

# === Main Application Class ===
class SubjectApp(ttk.Frame):
    def __init__(self, style: Style):
        super().__init__(style.master)

        self.style = style  # 🔑 store ttkbootstrap style

        self._setup_styles()

        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # === Label Frame for Form ===
        self.option_lf = ttk.Labelframe(self, text="Fill in the details", padding=15, style="Custom.TLabelframe")
        self.option_lf.pack(fill=X, padx=4, pady=4)

        # === Form Controls ===
        self.p_var = tk.StringVar(value="ALL")
        self.t_var = tk.StringVar(value="ALL")
        self.search_var = tk.StringVar()
        self.search_toggle_var = tk.BooleanVar(value=True)
        self.download_toggle_var = tk.BooleanVar(value=True)
        self.subjects_toggle_var = tk.BooleanVar(value=True)

        # === Header Container ===
        # header_frame = ttk.Frame(self.option_lf)
        # header_frame.pack(fill=X, padx=10, pady=(10, 5))

        # header_frame.columnconfigure(0, weight=3)  # Title
        # header_frame.columnconfigure(1, weight=1)  # Theme menu

        # header_label = ttk.Label(
        #     header_frame,
        #     text="📘 Subject Search & Export Tool",
        #     font=self.ui_font_label,
        #     bootstyle="primary"
        # )
        # header_label.grid(row=0, column=0, sticky=W)

        # self.theme_var = tk.StringVar(value="flatly")

        # self.theme_menu_btn = ttk.Menubutton(
        #     header_frame,
        #     textvariable=self.theme_var,
        #     direction="below",
        #     bootstyle="outline-secondary"
        # )
        # self.theme_menu_btn.grid(row=0, column=1, sticky=E)

        # theme_menu = tk.Menu(self.theme_menu_btn, tearoff=False)
        # self.theme_menu_btn["menu"] = theme_menu

        # available_themes = [
        #     "cosmo", "flatly", "journal", "litera",
        #     "lumen", "minty", "pulse", "sandstone",
        #     "united", "yeti", "morph", "simplex",
        #     "cerculean", "darkly", "superhero",
        #     "solar", "cyborg", "vapor"
        # ]

        # for theme in available_themes:
        #     theme_menu.add_command(
        #         label=theme.capitalize(),
        #         command=lambda t=theme: self._change_theme(t)
        #     )

        # === Row container ===
        row_frame = ttk.Frame(self.option_lf)
        row_frame.pack(fill=X, pady=5)

        # Configure column weights
        row_frame.columnconfigure(0, weight=1)  # Pathway (25%)
        row_frame.columnconfigure(1, weight=1)  # Track (25%)
        row_frame.columnconfigure(2, weight=2)  # Search (50%)

        # Create an empty menu for the Menubutton
        menu_font = tkFont.Font(family=fontFamilies["menu"], size=fontSize["medium"])

        # === Pathway Column ===
        pathway_frame = ttk.Frame(row_frame)
        pathway_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 2))

        # Label
        ttk.Label(pathway_frame, text="Select Pathway:").pack(anchor=W)

        # Menubutton
        self.p_menu_btn = ttk.Menubutton( pathway_frame, textvariable=self.p_var, direction="below", style="Custom.TMenubutton" )
        self.p_menu_btn.pack(fill=X)

        # Menu
        pathway_menu = tk.Menu(self.p_menu_btn, tearoff=False, font=menu_font)
        self.p_menu_btn["menu"] = pathway_menu

        # Populate menu items
        pathway_menu.add_command(
            label="ALL",
            command=lambda v="ALL": self._set_pathway(v)
        )

        for pathway in pathway_tracks.keys():
            pathway_menu.add_command(
                label=pathway,
                command=lambda v=pathway: self._set_pathway(v)
            )

        # === Track Column ===
        track_frame = ttk.Frame(row_frame)
        track_frame.grid(row=0, column=1, sticky="nsew", padx=(2, 2))

        # Label
        ttk.Label(track_frame, text="Select Track:").pack(anchor=W)

        # Menubutton
        self.t_menu = ttk.Menubutton( track_frame, textvariable=self.t_var, direction="below", style="Custom.TMenubutton" )
        self.t_menu.pack(fill=X)

        self.t_menu_menu = tk.Menu( self.t_menu, tearoff=False, font=menu_font )
        self.t_menu["menu"] = self.t_menu_menu

        # Default value
        self.t_var.set("ALL")

        # === Toggle Row ===
        toggle_row = ttk.Frame(self.option_lf)
        toggle_row.pack(fill=X, pady=(5, 8))

        # Column layout: 10% | 10% | 10% | 70%
        toggle_row.columnconfigure(0, weight=1)
        toggle_row.columnconfigure(1, weight=1)
        toggle_row.columnconfigure(2, weight=1)
        toggle_row.columnconfigure(3, weight=7)

        # Search Toggle
        self.search_toggle = ttk.Checkbutton(
            toggle_row,
            text="Enable Subject Search",
            variable=self.search_toggle_var,
            bootstyle="round-toggle",
            command=self._toggle_search_entry
        )
        self.search_toggle.grid(row=0, column=0, sticky=W)

        # Download Toggle
        self.download_toggle = ttk.Checkbutton(
            toggle_row,
            text= "Enable Download",
            variable=self.download_toggle_var,
            bootstyle="round-toggle",
            command=self._update_download_button_state
        )
        self.download_toggle.grid(row=0, column=1, sticky=E)

        # Subjects Toggle
        self.subjects_toggle_var = tk.BooleanVar(value=True)

        self.subjects_toggle = ttk.Checkbutton(
            toggle_row,
            state=DISABLED,
            text="Combine Subjects",
            variable=self.subjects_toggle_var,
            bootstyle="round-toggle",
            command=self._update_subject_state
        )
        self.subjects_toggle.grid(row=0, column=2, sticky=E)

        # Row Count Label
        self.row_count_var = tk.StringVar(value="0 SELECTIONS")
        self.row_count_label = ttk.Label(
            toggle_row,
            textvariable=self.row_count_var,
            anchor=E,
            bootstyle="info",
            font=self.ui_font_info
        )
        self.row_count_label.grid(row=0, column=3, sticky="nsew")

        # === Search Entry ===
        search_frame = ttk.Frame(row_frame)
        search_frame.grid(row=0, column=2, sticky="nsew", padx=(2, 0))

        ttk.Label(search_frame, text="Search Subjects (comma-separated):").pack(anchor=W)

        self.search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var
        )
        self.search_entry.pack(fill=X)
        self.search_entry.bind("<KeyRelease>", lambda e: self.update_table())

        # === Table ===
        self.table = ttk.Treeview(self, style="Custom.Treeview", columns=("NO", "CODE", "PATHWAY", "TRACK", "SUBJECT 1", "SUBJECT 2", "SUBJECT 3"), show="headings")
        for col in self.table["columns"]:
            self.table.heading(col, text=col)
            self.table.column(col, width=120, anchor=W)
        self.table.pack(fill=BOTH, expand=True, padx=8, pady=10)

        # Download Button
        self.download_btn = ttk.Button(self, text="📥 Download Excel", command=self.download_as_excel)
        self.download_btn.pack(fill=X, pady=8, padx=8)

        # Configure table layout
        self.update_tracks()
        self.update_table()
        self._toggle_search_entry()
        self._update_download_button_state()

    def update_tracks(self):
        pathway = self.p_var.get()

        # Clear existing menu
        self.t_menu_menu.delete(0, "end")

        # Determine tracks for this pathway
        if pathway == "ALL":
            tracks = ["ALL"]
        else:
            tracks = ["ALL"] + pathway_tracks.get(pathway, [])

        # Populate menu
        for track in tracks:
            self.t_menu_menu.add_command(
                label=track,
                command=lambda v=track: self._set_track(v)
            )

        # Reset selected value
        self.t_var.set("ALL")

        # Update table immediately if needed
        self.update_table()

    def update_table(self):
        pathway = self.p_var.get()
        track = self.t_var.get()
        keywords = [kw.strip().lower() for kw in self.search_var.get().split(',')] if self.search_toggle_var.get() else None

        for item in self.table.get_children():
            self.table.delete(item)

        records = process_raw_data(pathway, track, keywords)
        for record in records:
            self.table.insert("", "end", values=list(record.values()))

        auto_size_columns(self.table)

        # ✅ update row counter
        row_count = len(records)
        self.row_count_var.set(
            f"({row_count}) Available Selection{'s' if row_count != 1 else ''}".upper()
        )
        self._update_row_count_style(row_count)

    def download_as_excel(self):
        if not self.download_toggle_var.get():
            messagebox.showwarning( "Download Disabled", "Enable the download toggle to export data." )
            return
    
        pathway = self.p_var.get()
        track = self.t_var.get()
        keywords = [kw.strip().lower() for kw in self.search_var.get().split(',')] if self.search_toggle_var.get() else None

        records = process_raw_data(pathway, track, keywords)
        if not records:
            messagebox.showinfo("No Data", "No matching data to export.")
            return

        df = pd.DataFrame(records)
        file_name = f"{pathway}_{track}_FILTERED.xlsx".replace(" ", "_").upper()
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile=file_name)

        if file_path:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Success", f"File saved to: {file_path}")

    def _set_pathway(self, value):
        self.p_var.set(value)
        self.update_tracks()

    def _set_track(self, value):
        """Called when a track is selected from the Menubutton"""
        self.t_var.set(value)
        self.update_table()

    def _setup_styles(self):
        style = ttk.Style()

        # Base fonts
        self.ui_font = tkFont.Font(family=fontFamilies["default"], size=fontSize["default"])
        self.ui_font_header = tkFont.Font(family=fontFamilies["default"], size=fontSize["large"], weight="bold", underline=True)
        self.ui_font_label = tkFont.Font(family=fontFamilies["labels"], size=fontSize["large"], weight="bold", underline=False)
        self.ui_font_info = tkFont.Font(family=fontFamilies["text"], size=fontSize["xlarge"], underline=False)

        # Treeview
        style.configure( "Custom.Treeview", font=self.ui_font, rowheight=28, borderwidth=1, relief="solid" )
        style.configure( "Custom.Treeview.Heading", font=self.ui_font_header, borderwidth=1, relief="solid" )
        # Labelframe
        style.configure( "Custom.TLabelframe", font=self.ui_font_header, padding=10 )
        # Menubutton (button itself)
        style.configure( "Custom.TMenubutton", font=self.ui_font, padding=6 )
        # Text
        style.configure( "Custom.TText", font=self.ui_font_info )

    def _toggle_search_entry(self):
        """Enable/disable search entry based on toggle"""
        if self.search_toggle_var.get():
            self.search_entry.configure(state="normal")
        else:
            self.search_entry.configure(state="disabled")
            self.search_var.set("")        # clear search text
            self.update_table()            # refresh table

    def _update_row_count_style(self, row_count):
        search_text = self.search_var.get().strip()

        if row_count == 0:
            style = "danger"
        elif search_text:
            style = "primary"
        else:
            style = "info"

        self.row_count_label.configure(bootstyle=style)

    def _update_download_button_state(self):
        if self.download_toggle_var.get():
            self.download_btn.configure(
                state=NORMAL,
                text="📥 Download Excelsheet",
                bootstyle="success"
            )
        else:
            self.download_btn.configure(
                # state=DISABLED,
                text="⛔ Download Disabled",
                bootstyle="secondary"
            )

    def _update_subject_state(self):
        messagebox.showinfo(
            "Info",
            "This toggle is currently for future use and has no effect."
        )
        pass

    # def _change_theme(self, theme_name):
    #     self.theme_var.set(theme_name)
    #     self.style.theme_use(theme_name)

# === Launch App ===
if __name__ == "__main__":
    style = Style("flatly")  # Change theme here
    app = SubjectApp(style.master)
    app.master.title("Grade 10 Subject Selector Search & Export Tool")
    app.master.geometry("900x640")
    app.mainloop()
