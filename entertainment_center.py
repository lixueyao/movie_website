# coding=UTF-8
import media
import fresh_tomatoes

my_movies =[]
movies_info = [["神偷奶爸3 Despicable Me 3",
               "《神偷奶爸3》将延续前两部的温馨、搞笑风格，聚焦格鲁和露西的婚后生活",
               "https://img3.doubanio.com/view/photo/photo/public/p2469070974.webp",
               "https://www.youtube.com/watch?v=_UcRUrRIyDM"],
              ["加勒比海盗5：死无对证",
               "故事发生在《加勒比海盗3：世界的尽头》沉船湾之战20年后",
               "https://img3.doubanio.com/view/photo/photo/public/p2459723975.webp",
               "https://www.youtube.com/watch?v=mJcONgDxnd8"],
              ["悟空传 (2017)",
               "这不是西游记的任何章节，这是悟空的故事",
               "https://img1.doubanio.com/view/photo/photo/public/p2475060299.webp",
               "https://www.youtube.com/watch?v=BOD6blw4U_c"],
               ["神奇女侠 Wonder Woman (2017)",
                "戴安娜的女儿,而她的体内，似乎隐藏着某种强大的未知力量",
                "https://img3.doubanio.com/view/photo/photo/public/p2460006593.webp",
                "https://www.youtube.com/watch?v=h2MXZEUys10"],
               ["银河护卫队2 Guardians of the Galaxy Vol. 2 (2017)",
                "火箭浣熊偷走了大祭司阿耶莎的能量电池，包括星爵在内的一行人遭到了后者派出的舰队的袭击。一个神秘人物乘坐着飞船救下了银河护卫队的众人，而驾驶着飞船的不是别人，竟然正是星爵的亲生父亲伊戈",
                "https://img3.doubanio.com/view/photo/photo/public/p2454951206.webp",
                "https://www.youtube.com/watch?v=efpv3dvN8mI"],
               ["摔跤吧！爸爸 Dangal (2016)",
                "马哈维亚曾经是一名前途无量的摔跤运动员，在放弃了职业生涯后，他最大的遗憾就是没有能够替国家赢得金牌。马哈维亚将这份希望寄托在了尚未出生的儿子身上，哪知道妻子接连给他生了两个女儿，取名吉塔。让马哈维亚没有想到的是，两个姑娘展现出了杰出的摔跤天赋，让他幡然醒悟，就算是女孩，也能够昂首挺胸的站在比赛场上，为了国家和她们自己赢得荣誉",
                "https://img3.doubanio.com/view/photo/photo/public/p2457983084.webp",
                "https://www.youtube.com/watch?v=hYGQE5AZ4dE"]
              ]

print media.Movies.__init__.__doc__
print media.Movies.show_trailer.__doc__

for movie in movies_info:
    movie_info = media.Movies(movie[0], movie[1], movie[2], movie[3])
    my_movies.append(movie_info)

fresh_tomatoes.open_movies_page(my_movies)
