import functools

class Base:
    def __init__(self, name, produce_cost, produce_time, value, produce_count=1):
        self.name = name        # string
        self.cost = produce_cost / produce_count        # per one thing
        self.time = produce_time / produce_count
        self.value = value
    def __str__(self):
        return self.name

    @functools.total_ordering
    def __lt__(self, other):
        return str(self) < str(other)

class Compound:
    def __init__(self, name, ingredients, value, time):
        self.name = name
        self.ingredients = ingredients  # [(name, count)]
                                        # guarentee DAG
        self.time = time                # second: int
        self.value = value
    def __str__(self):
        return self.name
    
    @functools.total_ordering
    def __lt__(self, other):
        return str(self) < str(other)

def check_name(base_list, compound_list):
    from itertools import chain
    names = set()
    for i in chain(base_list, compound_list):
        names.add(i.name)
    for i in compound_list:
        for j in i.ingredients:
            if j[0] not in names:
                print(str(i))

base_list = [
    #    name         cost    time    value     count
    Base("瑞士卷木柴",  30,     30,      50,      3 ),
    Base("豆豆果凍",    50,     60,      89,      3 ),
    Base("方糖",       80,     90,      131,     3 ),
    Base("餅乾粉",     600,    1500,     547,    9 ),
    Base("果凍莓",     1500,   2160,     1513,   6 ),
    Base("香醇牛奶",    700,    1800,     1865,   2 ),
    Base("棉花糖羊毛",  1000,   5400,     8029,   1 ),
]

compound_list = [
    #       value    time(second)
    # 鏗鏘打鐵鋪
    Compound('堅硬斧頭', [('瑞士卷木柴', 2)],
            123,      30),
    Compound('堅固的十字鎬', [('瑞士卷木柴', 3), ('方糖', 3)],
            672,     180),
    Compound('銳利的鋸子', [('瑞士卷木柴', 6), ('方糖', 5)],
            1348,     420),
    Compound('耐用的鏟子', [('瑞士卷木柴', 10), ('方糖', 10)],
            2545,     900),
    Compound('神秘蝴蝶餅木樁', [('瑞士卷木柴', 15), ('方糖', 15)],
            5889,     3600),
    Compound('藍色糖果鉗子', [('瑞士卷木柴', 22), ('方糖', 18)],
            11871,    10800),
    Compound('恆久的糖衣槌子', [('瑞士卷木柴', 30), ('方糖', 35)],
            18045,    21600),

    # 極甜果醬坊
    Compound('豆豆果凍果醬', [('豆豆果凍', 3)],
            351,      90),
    Compound('甜甜果凍果醬', [('豆豆果凍', 6)],
            1256,     480),
    Compound('椪糖果醬', [('豆豆果凍', 6), ('紮實的黑麥麵包', 2)],
            4728,     1200),
    Compound('石榴果醬', [('豆豆果凍', 16), ('果凍拿鐵', 1)],
            13343,    7200),
    # Compound('跳跳莓果醬', [],
    #         0,    0),

    # 熱騰騰麵包坊
    Compound('紮實的黑麥麵包', [('豆豆果凍果醬', 1), ('餅乾粉', 2)],
            2422,      720),
    Compound('香甜果醬派', [('豆豆果凍', 6), ('餅乾粉', 3)],
            3516,      1200),
    Compound('銀杏佛卡夏', [('餅乾粉', 6), ('熊熊果凍漢堡', 1)],
            6475,      1800),
    Compound('糖霜甜甜圈', [('方糖', 15), ('亮晶晶玻璃片', 1)],
            7604,      3600),
    Compound('柔軟的蜂蜜蛋糕', [('奶油', 1), ('滑嫩蛋包飯', 1)],
            25307,      10800),
    # Compound('金黃可頌', [('香醇牛奶', 12), ('玻璃捧花', 1)],
    #         0,      21600),

    # 瑞士捲工坊
    Compound('松果鳥娃娃', [('瑞士卷木柴', 6)],
            788,      300),
    Compound('橡實桌燈', [('瑞士卷木柴', 12), ('果凍莓', 3)],
            5014,      1320),
    Compound('咕咕鐘', [('餅乾粉', 8), ('椪糖果醬', 4)],     
            15959,      7200),
    Compound('天鵝羽毛捕夢網', [('棉花糖羊毛', 1), ('棒棒糖花籃', 1)],
            25935,      12600),

    # 果醬派餐廳
    Compound('暖呼呼的果凍燉湯', [('豆豆果凍', 4), ('果凍莓', 1)],
            3183,      1080),
    Compound('熊熊果凍漢堡', [('豆豆果凍', 10), ('香甜果醬派', 1)],
            4557,      1320),
    Compound('糖果奶油義大利麵', [('餅乾粉', 7), ('鮮奶油', 1)],
            8802,      3000),
    Compound('滑嫩蛋包飯', [('果凍莓', 6), ('銀杏佛卡夏', 1)],
            13391,      5400),
    # Compound('什錦披薩果凍', [('果凍莓', 10), ('奶油根汁啤酒', 1)],
    #         0,      12600),
    # Compound('高級的果凍套餐', [],
    #         0,      25200),

    # 樂樂陶工坊
    Compound('餅乾花盆', [('松果鳥娃娃', 2), ('餅乾粉', 4)],
            4119,      900),
    Compound('亮晶晶玻璃片', [('方糖', 12), ('暖呼呼的果凍燉湯', 1)],
            6634,      1620),
    Compound('閃耀的彩色彈珠', [('橡實桌燈', 1), ('棉花糖羊毛', 1)],
            15975,      7200),
    # Compound('彩虹點心盅', [('方糖', 15), ('什錦披薩果凍', 1)],
    #         26943,      18000),

    # 幸福花坊
    Compound('糖果花', [('果凍莓', 2), ('餅乾花盆', 1)],
            5570,      1200),
    Compound('幸福花盆', [('果凍莓', 4), ('方糖', 10)],
            8180,      1800),
    Compound('糖果花束', [('果凍莓', 5), ('糖果奶油義大利麵', 1)],
            1000,      3600),
    Compound('棒棒糖花籃', [('閃耀的彩色彈珠', 1), ('豆豆果凍', 18)],
            17778,      9000),
    Compound('玻璃捧花', [('雲朵糖抱枕', 2), ('豆豆果凍', 20)],
            24620,      16200),
    # Compound('別緻的優格花環', [('豆豆果凍', 30), ('跳跳莓果醬', 2)],
    #         0,      27000),

    # 香醇牛奶作坊
    Compound('鮮奶油', [('甜甜果凍果醬', 1), ('香醇牛奶', 2)],
            5977,      1740),
    Compound('奶油', [('香醇牛奶', 3), ('石榴果醬', 1)],
            21011,      9000),
    # Compound('手工起司', [('香醇牛奶', 10), ('咕咕鐘', 1)],
    #         0   ,      16200),

    # Cafè Latte
    Compound('果凍拿鐵', [('豆豆果凍', 12), ('香醇牛奶', 2)],
            7569,      3600),
    Compound('珍珠奶茶', [('果凍莓', 8), ('糖霜甜甜圈', 1)],
            19655,      10800),
    # Compound('甜莓汽水', [('果凍莓', 12), ('彩虹點心盅', 1)],
    #         0   ,      23400),

    # 可愛娃娃工坊
    Compound('雲朵糖抱枕', [('糖果花', 1), ('棉花糖羊毛', 1)],
            14722,      5400),
    Compound('熊熊果凍娃娃', [('糖果花束', 2), ('棉花糖羊毛', 1)],
            24806,      14400),
    # Compound('火龍果龍族娃娃', [],
    #         0   ,      25200),

    # 木桶休憩所
    Compound('奶油根汁啤酒', [('餅乾粉', 10), ('幸福花盆', 1)],
            17805,      9000),
    # Compound('紅莓汁', [],
    #         0   ,      21600),
    # Compound('陳年野篸飲', [],
    #         0   ,      28800),

    # 左岸法式點心坊
    Compound('陰森森的馬芬蛋糕', [('餅乾粉', 12), ('香醇牛奶', 7)],
            19615,      12600),
    # Compound('新鮮草莓蛋糕', [('餅乾粉', 14), ('珍珠奶茶', 2)],
    #         0   ,      21600),
    # Compound('派對戚風蛋糕', [],
    #         0   ,      28800),

    # 金緻珠寶店
#     Compound('糖衣戒指', [('餅乾粉', 12), ('柔軟的蜂蜜蛋糕', 1)],
#             0   ,      18000),
#     Compound('紅寶石莓胸針', [('果凍莓', 16), ('黃金可頌', 2)],
#             0   ,      27000),
#     Compound('皇家熊熊果凍王冠', [],
#             0   ,      28800)
]

# check_name(base_list, compound_list)
