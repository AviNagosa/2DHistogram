from src.histogram import *

def main():

    Map = [['G', 'G', 'G'],       #world
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]

    measurements = ['R','R']

    motions = [[0,0],[0,1]]             #motions[0] move -> right, motions[1] -> stay
    sensor_right = 1.0           #robot sensor probability
    p_move = 1.0                     #robot move probability
    ans = histogram_localization(Map, measurements, motions, sensor_right, p_move)
    show(ans) # displays your answer
    print(ans[0])
    print('\n')
    test1()



def test1():
    p = [0.2, 0.2, 0.2, 0.2, 0.2]
    world = ['G', 'R', 'R', 'G', 'G']
    Z = 'G'
    pHit = 0.6
    pMiss = 0.2

    def sense1(p, Z):
        q1 = []
        for i in range(len(p)):
            hit = (Z == world[i])
            q1.append(p[i] * (hit * pHit + (not hit) * pMiss))
        return q1

    print("Apriori Dist:")
    print(p)
    print("Aposteriori:")
    p=sense1(p, Z)
    print(p)
    print (sum(p))



if __name__ == '__main__':
    main()


