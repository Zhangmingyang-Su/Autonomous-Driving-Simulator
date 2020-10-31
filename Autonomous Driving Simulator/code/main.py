import pandas as pd
from transformation import path_leaf, remove, load_img_steering
from sklearn.model_selection import train_test_split
from preprocessing import batch_generator
from nvidia import nvidia_model

def model_application():
    datadir = 'track'
    columns = ['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed']
    data = pd.read_csv(os.path.join(datadir, 'driving_log.csv'), names = columns)
    pd.set_option('display.max_colwidth', -1)

    data["center"] = data["center"].apply(path_leaf)
    data["left"] = data["left"].apply(path_leaf)
    data["right"] = data["right"].apply(path_leaf)

    num_bins = 25
    samples_per_bin = 400
    hist, bins = np.histogram(data['steering'], num_bins)
    center = (bins[:-1]+ bins[1:]) * 0.5

    remove_list = remove(num_bins, bins, samples_per_bin, data["steering"])
    data = data.drop(data.index[remove_list], inplace=True)

    image_paths, steerings = load_img_steering(datadir + '/IMG', data)
    X_train, X_valid, y_train, y_valid = train_test_split(image_paths, steerings, test_size=0.2, random_state=6)

    x_train_gen, y_train_gen = next(batch_generator(X_train, y_train, 1, 1))
    x_valid_gen, y_valid_gen = next(batch_generator(X_valid, y_valid, 1, 0))

    model = nvidia_model()

    history = model.fit_generator(batch_generator(X_train, y_train, 100, 1),
                                  steps_per_epoch=300,
                                  epochs=10,
                                  validation_data=batch_generator(X_valid, y_valid, 100, 0),
                                  validation_steps=200,
                                  verbose=1,
                                  shuffle = 1)
if __name__ == '__main__':
    model_application()
    model.save('model.av')
