from brise_plandok.annotation_process.utils.constants import DOC_HEADER
import pandas


def load_doc_tracking_data(file):
    dtype = {
        DOC_HEADER[0]: int,
        DOC_HEADER[1]: str,
        DOC_HEADER[2]: bool,
        DOC_HEADER[3]: bool,
        DOC_HEADER[4]: int,
        DOC_HEADER[5]: str,
        DOC_HEADER[6]: str,
        DOC_HEADER[7]: bool,
    }
    return pandas.read_csv(filepath_or_buffer=file, sep=";", dtype=dtype)


def save_doc_tracking_data(file, df):
    df.to_csv(path_or_buf=file, sep=";", index=False)


def get_next_batch(df, batch_size, set_assigned, phase):
    first = _get_first_not_assigned(df, phase)
    if set_assigned:
        _set_assigned_true(df, first, batch_size, phase)
    return _get_next_batch_doc_ids(df, first, batch_size)


def _get_assigned_doc_header(phase):
    return DOC_HEADER[2] if phase == 1 else DOC_HEADER[7]


def _get_first_not_assigned(df, phase):
    order_col = DOC_HEADER[0]
    assigned_col = _get_assigned_doc_header(phase)
    return df[df[assigned_col] == False].iloc[0][order_col]


def _set_assigned_true(df, first, batch_size, phase):
    order_col = DOC_HEADER[0]
    assigned_col = _get_assigned_doc_header(phase)
    mask = (df[order_col] >= first) & (df[order_col] < first + batch_size)
    df.loc[mask, assigned_col] = True


def _get_next_batch_doc_ids(df, first, batch_size):
    order_col = DOC_HEADER[0]
    doc_id_col = DOC_HEADER[1]
    return list(df[doc_id_col][(df[order_col] >= first) & (df[order_col] < first + batch_size)])
