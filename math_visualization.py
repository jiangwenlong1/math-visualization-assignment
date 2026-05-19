import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='y = x', linestyle='-')
plt.plot(x, y2, label='y = x²', linestyle='--')
plt.plot(x, y3, label='y = sin(x)', linestyle=':')
plt.plot(x, y4, label='y = e^(-0.1x) * cos(x)', linestyle='-.')


plt.title('Mathematical Function Visualization')
plt.xlabel('x values')
plt.ylabel('y values')

plt.legend()
plt.grid(True)

plt.savefig('function_plot.png')
plt.show()


x2 = np.linspace(-10, 10, 200)

y_custom = np.log(x2**2 + 1) * np.cos(x2) + 0.2 * x2

plt.figure(figsize=(10, 6))

plt.plot(x2, y_custom, label='Custom Equation')

plt.title('Own Equation Visualization')
plt.xlabel('x values')
plt.ylabel('y values')

plt.grid(True)
plt.legend()

plt.savefig('own_equation.png')
plt.show()

students = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
midterm = [85, 72, 90, 66, 78, 92, 60, 74, 88, 95]
final = [80, 70, 94, 68, 75, 90, 65, 72, 84, 96]


total = []

for i in range(len(students)):
    score = 0.4 * midterm[i] + 0.6 * final[i]
    total.append(score)


plt.figure(figsize=(8, 6))
plt.scatter(midterm, final)

plt.title('Midterm vs Final Scores')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')
plt.grid(True)

plt.savefig('score_scatter.png')
plt.show()



plt.figure(figsize=(8, 6))
plt.hist(total, bins=5)

plt.title('Distribution of Total Scores')
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.grid(True)

plt.savefig('score_histogram.png')
plt.show()


plt.figure(figsize=(10, 6))
plt.bar(students, total)

plt.title('Student Total Scores')
plt.xlabel('Students')
plt.ylabel('Total Score')
plt.grid(True)

plt.savefig('score_bar_chart.png')
plt.show()

lope, intercept = np.polyfit(midterm, final, 1)

x_line = np.array([50, 100])
y_line = slope * x_line + intercept

plt.figure(figsize=(8, 6))


plt.scatter(midterm, final, label='Original Data')


plt.plot(x_line, y_line, label='Best-Fit Line')


plt.title('Score Prediction with Best-Fit Line')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')


plt.legend()
plt.grid(True)


plt.savefig('score_prediction.png')
plt.show()


predict_50 = slope * 50 + intercept
predict_75 = slope * 75 + intercept
predict_100 = slope * 100 + intercept

print('Predicted final score for midterm 50:', round(predict_50, 2))
print('Predicted final score for midterm 75:', round(predict_75, 2))
print('Predicted final score for midterm 100:', round(predict_100, 2))
