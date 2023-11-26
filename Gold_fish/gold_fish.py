from random import randint

class gold_fish:
    life = 0  #ライフであり水質（水の透明度,白いフィルター）
    size = 10
    color = 10
    count = 16
    fish_die = False
    
    def __init__(self):
        self.life = 0  #ライフであり水質（水の透明度,白いフィルター）
        self.size = 10
        self.color = 10
        self.count = 16
        self.fish_die = False

    def die_judge(self):
            if(self.life >= 90):
                self.fish_die = True

    def counter(self):
        #育成ターン経過
        print("ターン経過前：{}".format(self.count))#デバック用
        self.count -= 1
        print("ターン経過：{}".format(self.count))#デバック用

        #ターン経過時に水も汚れる
        print("水質変化前：{}".format(self.life))#デバック用
        self.life += randint(5,20)
        print("水質変化後：{}".format(self.life))#デバック用
        
    def use_worm(self):
        self.size += 6
        gold_fish.counter(self)

    def use_food(self):
        self.color += 10
        gold_fish.counter(self)

    def use_water(self):
        self.life -= 20
        gold_fish.counter(self)

    