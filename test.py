from utils import Brush, Painting

x_dim = 100
y_dim = 100
dim = (x_dim, y_dim)
brushes = [Brush(x_dim, y_dim) for i in range(5)]
iterations = 1000

painting = Painting(dim, brushes, iterations)
painting.generate_data()    
painting.plot_data()