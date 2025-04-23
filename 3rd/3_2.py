##change element
basketball_player = ['James', 'Kobe', 'Curry', 'Wade']
print(basketball_player[0])
basketball_player[0] = 'Durant'
print(basketball_player[0])

##append 对列表进行添加元素操作
basketball_player = ['James', 'Kobe', 'Curry', 'Wade']
basketball_player.append('Butler')
print(basketball_player)

football_player = []
football_player.append('Messi')
football_player.append('Havertz')
football_player.append('Neymer')
print(football_player)

##insert element
football_player.insert(1,'Ronaldo')
print(football_player)

##del element
del football_player[1]
print(football_player)

##pop的用法就是栈，.pop()输出列表最后一个元素。
basketball_player = ['James', 'Kobe', 'Curry', 'Wade']
print(basketball_player)
flash = basketball_player.pop()
print(flash)
print(basketball_player)

##不再用就del,要继续用就pop赋值

##remove:按照字符串索引；del:按照位置索引;remove后可以使用
basketball_player = ['James', 'Kobe', 'Curry', 'Wade']
print(basketball_player)
fakegoat = basketball_player.pop(0)
deadplayer = 'Kobe'
basketball_player.remove(deadplayer)
print(fakegoat)
print(basketball_player)

