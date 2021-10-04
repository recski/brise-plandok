# Development

## Modify labels

- In the xlsx templates [BRISE.xlsx](./brise_plandok/annotation/BRISE.xlsx) and [review_template.xlsx](./brise_plandok/review/input/review_template.xlsx)
    - change labels on the labels tab
    - if you also added or deleted labels you also have to adjust the `Named Ranges` (in LibreOffice: `Sheet > Named Ranges and Expressions`)
    - Click to the first sheet and save the document.
        - Explanation: for some code the active tab is used, which is always the last saved one.

- Adjust the categories in [merkmale_categories.csv](./brise_plandok/annotation/merkmale_categories.csv)