import pandas as pd


if __name__ == "__main__":
    print('start program')
    gan_better = []
    human_better = []
    names_gan_with = ['689514930','1edit_blur','5_blur','6_blur','bzong_blur']
    names_gan_without = ['1edit_r','5_r','6_r','bzong_r']
    names_gan = names_gan_with + names_gan_without
    df = pd.read_csv("2020-09-13 08-45-00.csv")

    l_names = df['Left Image'].to_list()
    r_names = df[' Right Image'].to_list()
    scores = df[' Better One (0 - Left; 1 - Equal; 2 - Right)'].to_list()
    left_gan = [False] * len(df)
    right_gan = [False] * len(df)

    for i,l in enumerate(l_names):
        for name in names_gan:
            if name in l:
                left_gan[i] = True

    for i,r in enumerate(r_names):
        for name in names_gan:
            if name in r:
                right_gan[i] = True

    for i,s in enumerate(scores):
        if left_gan[i] == right_gan[i]:
            continue

        if s==1:
            continue
        elif s==0:
            if left_gan[i] and not right_gan[i]:
                gan_better.append(i)
            elif not left_gan[i] and right_gan[i]:
                human_better.append(i)
        elif s==2:
            if left_gan[i] and not right_gan[i]:
                human_better.append(i)
            elif not left_gan[i] and right_gan[i]:
                gan_better.append(i)

    print(len(df))
    print(len(human_better))
    print(len(gan_better))



    print('end program')