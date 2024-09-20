import numpy as np
import matplotlib.pyplot as plt
import unittest

# Визначення функцій Лоренца
def lorenz_system(x, y, z, sigma=10, rho=28, beta=8/3): # В параметрах записанні сталі для атрактора
    # Функція обчислює похідні системи Лоренца в даний момент часу
    dx_dt = sigma * (y - x)  # Похідна по x
    dy_dt = x * (rho - z) - y # По y
    dz_dt = x * y - beta * z # По z
    return dx_dt, dy_dt, dz_dt

def run_lorenz(initial_state, num_steps=10000, dt=0.01):
    # Функція для симуляції системи Лоренца на задану кількість кроків
    x, y, z = initial_state
    trajectory = np.zeros((num_steps, 3))  # Масив для зберігання траєкторії
    trajectory[0] = x, y, z  # Початкове значення

    for i in range(1, num_steps):
        # Обчислення похідних
        dx_dt, dy_dt, dz_dt = lorenz_system(x, y, z)
        # Оновлення стану системи
        x += dx_dt * dt
        y += dy_dt * dt
        z += dz_dt * dt
        trajectory[i] = x, y, z  # Збереження нових значень у траєкторію
        
    return trajectory

def plot_lorenz(trajectories):
    # Функція для побудови графіків траєкторій Лоренца
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for traj in trajectories:
        ax.plot(traj[:, 0], traj[:, 1], traj[:, 2])  # Побудова 3D ліній
    ax.set_xlabel('X axis')  # Підпис осей
    ax.set_ylabel('Y axis')  
    ax.set_zlabel('Z axis')  
    plt.title('Lorenz Attractor')  # Заголовок графіку
    plt.show()


class TestLorenzSystem(unittest.TestCase):
    def test_lorenz_system(self):
        # Тест для перевірки функції lorenz_system
        x, y, z = 1.0, 1.0, 1.0
        dx_dt, dy_dt, dz_dt = lorenz_system(x, y, z)
        self.assertAlmostEqual(dx_dt, 0.0)  # Очікуване значення похідної по x
        self.assertAlmostEqual(dy_dt, 26.0)  # Очікуване значення похідної по y
        self.assertAlmostEqual(dz_dt, -1.6666666666666667)  # Очікуване значення похідної по z

    def test_run_lorenz(self):
        # Тест для перевірки функції run_lorenz
        initial_state = [0.0, 1.0, 1.05]
        # Запускаємо модель Лоренца для початкового стану initial_state і виконуємо лише один крок симуляції (num_steps=1) з кроком часу dt=0.01
        trajectory = run_lorenz(initial_state, num_steps=1, dt=0.01)
        
        # Перевіряємо, що розмір траєкторії відповідає очікуваному (1 крок, 3 координати)
        self.assertEqual(trajectory.shape, (1, 3))
        
        # Перевіряємо, що перший елемент траєкторії відповідає початковому стану (x, y, z)
        self.assertAlmostEqual(trajectory[0, 0], 0.0)  # Початкове значення x
        self.assertAlmostEqual(trajectory[0, 1], 1.0)  # Початкове значення y
        self.assertAlmostEqual(trajectory[0, 2], 1.05)  # Початкове значення z


    def test_trajectory_divergence(self):
        # Тест для перевірки чутливості до початкових умов
        initial_state1 = [0.0, 1.0, 1.05]  # Початковий стан 1
        initial_state2 = [0.0, 1.0, 1.050001]  # Початковий стан 2, наближений до 1
        
        # Запуск моделі для обох початкових станів
        trajectory1 = run_lorenz(initial_state1)
        trajectory2 = run_lorenz(initial_state2)
        
        # Перевірка значного розходження траєкторій
        # Обчислюємо різницю між кінцевими станами двох траєкторій
        # Якщо різниця буде > 1, то чутливість до поч. умов підтверджується
        self.assertGreater(np.linalg.norm(trajectory1[-1] - trajectory2[-1]), 1.0)


# Основний код
if __name__ == "__main__":
    initial_state1 = [0.0, 1.0, 1.05]  # Початковий стан 1
    initial_state2 = [0.0, 1.0, 1.050001]  # Початковий стан 2, наближений до 1
    # Запуск моделі для обох початкових станів
    trajectory1 = run_lorenz(initial_state1)
    trajectory2 = run_lorenz(initial_state2)

    # Побудова графіку обох траєкторій
    plot_lorenz([trajectory1, trajectory2])

    # Запуск тестів
    unittest.main(argv=[''], exit=False)
