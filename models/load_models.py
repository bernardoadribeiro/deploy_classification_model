import bz2file as bz2
import pickle


def compress_pickle(filename:str, model):
    """
        Creates a file from pickle file with compressed size.
        The file generated is named as `filename.pbz2`

        params: 
            - filename: Expect a string that defines the filename
            - model: Expect a pickle file (*.pkl)
    """
    with bz2.BZ2File(filename + '.pbz2', 'w') as file:
        pickle.dump(model, file)


def decompress_pickle(model):
    """
        Decompress and load the model and return the model file from pickle file compressed.
        param: 
            - model -> Expect a pbz2 file (pickle compresseed file) (*.pbz2)
    """
    data = bz2.BZ2File(model, 'rb')
    data = pickle.load(data)

    return data


# # Compress the model to upload to git
# compress_pickle('productcategory_randtree_ros', 
#                 pickle.load(open('productcategory_randtree_ros.pkl', 'rb'))
#             )

