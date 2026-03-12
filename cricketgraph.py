import matplotlib.pyplot as plt
import numpy as np

players = ["Player1","Player2","Player3","Player4","Player5","Player6"]

runs = [450,520,610,480,550,600]
wickets = [15,20,18,22,17,19]
matches = [12,14,15,13,14,16]

performance = np.array([
[45,50,60,55,70,65],
[40,48,55,50,60,62],
[50,60,65,58,72,68],
[42,47,53,49,57,61],
[46,52,58,54,63,66],
[44,49,56,52,61,64]
])

plt.figure(figsize=(18,12))

# 1 Runs Line Graph
plt.subplot(3,3,1)
plt.plot(players,runs,marker="o",color="blue",linewidth=2)
plt.title("Player Runs Performance")
plt.grid(True)

# 2 Wickets Bar Chart
plt.subplot(3,3,2)
plt.bar(players,wickets,color="orange")
plt.title("Player Wickets Comparison")

# 3 Matches Played
plt.subplot(3,3,3)
plt.bar(players,matches,color="green")
plt.title("Matches Played")

# 4 Pie Chart (Runs Distribution)
plt.subplot(3,3,4)
plt.pie(runs,labels=players,autopct='%1.1f%%',
        colors=["purple","cyan","orange","green","red","blue"])
plt.title("Runs Distribution by Player")

# 5 Runs Distribution Histogram
plt.subplot(3,3,5)
plt.hist(runs,bins=5,color="red")
plt.title("Runs Distribution")

# 6 Area Chart
plt.subplot(3,3,6)
plt.fill_between(players,runs,color="skyblue")
plt.title("Runs Area Chart")

# 7 Step Chart
plt.subplot(3,3,7)
plt.step(players,wickets,color="brown",linewidth=2)
plt.title("Wickets Step Chart")

# 8 Box Plot
plt.subplot(3,3,8)
plt.boxplot(runs,patch_artist=True,
            boxprops=dict(facecolor="lime"))
plt.title("Runs Box Plot")

# 9 Heatmap
plt.subplot(3,3,9)
plt.imshow(performance,cmap="coolwarm",aspect="auto")
plt.colorbar()
plt.xticks(range(6),players)
plt.yticks(range(6),["Match1","Match2","Match3","Match4","Match5","Match6"])
plt.title("Player Performance Heatmap")

plt.suptitle("Cricket Player Performance Analysis Dashboard",fontsize=20)

plt.subplots_adjust(
top=0.92,
bottom=0.06,
left=0.06,
right=0.97,
hspace=0.40,
wspace=0.25
)

plt.show()