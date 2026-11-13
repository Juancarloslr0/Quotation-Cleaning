from pathlib import Path

import pandas as pd


HEADERS = [
    "Unnamed: 0",
    "CSI",
    "Labor Code",
    "Scope Description",
    "Bid Form QTY",
    "Bid Form UOM",
    "QTY",
    "UOM",
    "Unit Rate",
    "Total",
    "Comments/ Notes",
    "GS",
]


def main():
    rows = [
        ["", "", "", "General Conditions", "", "", "", "", "", "", "", ""],
        ["", "", "", "Mobilization", "", "", 1, "LS", 5000, 5000, "", ""],
        ["", "", "", "Site protection", "", "", 1, "LS", 1200, 1200, "", ""],
        ["", "", "", "Temporary fencing", "", "", 100, "LF", 15, 1500, "", ""],
        ["", "", "", "Temporary fencing", "", "", 50, "LF", 15, 750, "", ""],
        ["", "", "", "Existing conditions survey", "", "", 1, "LS", 700, 700, "", ""],
        ["", "", "", "Mechanical", "", "", "", "", "", "", "", ""],
        ["", "", "", "Demolish existing piping", "", "", 200, "LF", 8, 1600, "", ""],
        ["", "", "", "Install copper piping", "", "", 100, "LF", 25, 2500, "", ""],
        ["", "", "", "Install copper piping", "", "", 40, "LF", 25, 1000, "", ""],
        ["", "", "", "Pipe insulation", "", "", 140, "LF", "$-", "", "", ""],
        ["", "", "", "System startup", "", "", 1, "LS", 1500, 1500, "", ""],
        ["", "", "", "Replace control valve", "", "", "TBD", "EA", 350, "", "", ""],
        ["", "", "", "Pump alignment", "", "", 2, "EA", 350, 700, "", ""],
        ["", "", "", "Electrical", "", "", "", "", "", "", "", ""],
        ["", "", "", "Install conduit", "", "", 120, "LF", 12, 1440, "", ""],
        ["", "", "", "Test wiring", "", "", 1, "LS", 900, 900, "", ""],
        ["", "", "", "Temporary fencing", "", "", 20, "LF", 20, 400, "", ""],
        ["", "", "", "Install LED fixtures", "", "", 15, "EA", 85, 1275, "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "Sub Total", "", "", "", "", "", "", "", ""],
        ["", "", "", "Mark Ups", "", "", "", "", "", "", "", ""],
        ["", "", "", "Package Total", "", "", "", "", "", "", "", ""],
    ]

    title_row = ["FICTIONAL SAMPLE QUOTATION"] + [""] * (len(HEADERS) - 1)
    spreadsheet_rows = [title_row, HEADERS, *rows]

    output_path = (
        Path(__file__).resolve().parents[1] / "data" / "sample_input.xlsx"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(spreadsheet_rows).to_excel(
        output_path,
        index=False,
        header=False,
        sheet_name="Quotation",
        engine="openpyxl",
    )
    print(f"Sample Excel created: {output_path}")


if __name__ == "__main__":
    main()
