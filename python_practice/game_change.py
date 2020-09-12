class TongLao():
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_peolpe(self, name):
        if name == 'WZY':
            print("师弟！！！！")
        elif name == '李秋水':
            print("呸，贱人")
        elif name == '丁春秋':
            print("叛徒！我要杀了你")

    def fight_zms(self, enemy_hp, enemy_power):
        self.hp *= 10
        self.power /= 2
        while True:
            self.hp = self.hp - enemy_power
            enemy_hp = enemy_hp - self.power
            if self.hp <= 0:
                print("You Won.", "my_hp", self.hp, "enemy_hp", enemy_hp)
                break
            elif enemy_hp <= 0:
                print("I win", "my_hp", self.hp, "enemy_hp", enemy_hp)
                break

class Xuzhu(TongLao):
    def __init__(self, hp, power):
        super(Xuzhu, self).__init__(hp, power)

    def read(self):
        print("罪过罪过")


xiaotong = TongLao(1000, 20)
xiaotong.fight_zms(300, 200)