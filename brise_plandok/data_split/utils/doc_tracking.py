from brise_plandok.data_split.utils.constants import DOC_HEADER
import pandas


def load_doc_tracking_data(file):
    dtype = {
        DOC_HEADER[0]: int,
        DOC_HEADER[1]: str,
        DOC_HEADER[2]: bool,
        DOC_HEADER[3]: bool,
        DOC_HEADER[4]: int,
    }
    return pandas.read_csv(filepath_or_buffer=file, sep=";", dtype=dtype)

def save_doc_tracking_data(file, df):
    df.to_csv(path_or_buf=file, sep=";", index=False)

def get_next_batch(df, batch_size, set_assigned=False):
    first = _get_first_not_assigned(df)
    if set_assigned:
        _set_assigned_true(df, first, batch_size)
    return _get_next_batch_doc_ids(df, first, batch_size)

def _get_first_not_assigned(df):
    order_col = DOC_HEADER[0]
    assigned_col = DOC_HEADER[2]
    return df[df[assigned_col] == False].iloc[0][order_col]


def _set_assigned_true(df, first, batch_size):
    order_col = DOC_HEADER[0]
    assigned_col = DOC_HEADER[2]
    df[assigned_col][(df[order_col] >= first) & (
        df[order_col] < first + batch_size)] = True


def _get_next_batch_doc_ids(df, first, batch_size):
    order_col = DOC_HEADER[0]
    doc_id_col = DOC_HEADER[1]
    return list(df[doc_id_col][(df[order_col] >= first) & (df[order_col] < first + batch_size)])
