from purchases.models import Purchase
from django.http import HttpRequest
from datetime import date
import pandas as pd
import plotly.express as px


class Analise:
    def __init__(self) -> None:
        self.__purchase = Purchase

    def return_json_purchase_by_user(self, request: HttpRequest) -> dict:
        purchases = self.__purchase.objects.filter(user=request.user)
        purchases_list = [
            {
                "name": purchase.name,
                "price": purchase.price,
                "category": purchase.category,
                "credit_card": purchase.credit_card,
                "description": purchase.description,
                "data_of_purchase": purchase.data_of_purchase,
            }
            for purchase in purchases
        ]
        return purchases_list

    def analyse_current_month_and_last_month(self, request: HttpRequest):
        current_month = date.today().month
        last_month = current_month - 1 if current_month != 1 else 12
        purchases = self.return_json_purchase_by_user(request)

        purchases = pd.DataFrame(purchases)
        purchases["month"] = purchases["data_of_purchase"].apply(
            lambda x: x.month
        )
        purchases = purchases[
            purchases["month"].isin([current_month, last_month])
        ]

        agregate_dataframe = (
            purchases[["month", "price", "category"]]
            .groupby(["month", "category"])
            .sum()
        ).reset_index()

        df_last_month = agregate_dataframe[
            agregate_dataframe["month"] == last_month
        ]
        df_current_month = agregate_dataframe[
            agregate_dataframe["month"] == current_month
        ]

        merged_df = df_last_month.merge(
            df_current_month,
            on="category",
            suffixes=("_last_month", "_current_month"),
            how="left",
        )
        merged_df = merged_df.fillna(0)
        merged_df["percent_difference"] = (
            (merged_df["price_current_month"] - merged_df["price_last_month"])
            / merged_df["price_last_month"]
        ) * 100

        merged_df["percent_difference_abs"] = (
            merged_df["percent_difference"].abs().astype("float").round(2)
        )
        final_dataframe = merged_df[
            [
                "category",
                "price_last_month",
                "price_current_month",
                "percent_difference",
                "percent_difference_abs",
            ]
        ].to_dict(orient="records")

        return final_dataframe


class Graph:
    def __init__(self) -> None:
        pass

    def scatter(self, df: pd.DataFrame, title: str, **kwargs) -> any:
        fig = px.scatter(df, **kwargs)
        fig.update_layout(
            title_text=title,
            title_x=0.45,  # Define o título no meio horizontal do gráfico (0 a 1)
            title_font=dict(
                size=30, family="Arial, sans-serif", color="black"
            ),
        )
        fig.update_layout(height=700)
        chart = fig.to_html()

        return chart
