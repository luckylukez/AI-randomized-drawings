from utils import StraightBrush, Painting

def main():
    x_dim = 100
    y_dim = 100
    dim = (x_dim, y_dim)
    brushes = [StraightBrush(x_dim, y_dim) for i in range(5)]
    iterations = 150

    painting = Painting(dim, brushes, iterations)
    painting.generate_data()
    painting.plot_data()
    painting.generate_gif()

if __name__ == '__main__':
    main()