import os


def get_labels_df_path(sub_dir):
    return os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_labels.csv")


def get_features_df_path(sub_dir):
    return os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_features.csv")


def get_data_df_path(sub_dir):
    return os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_data.csv")
