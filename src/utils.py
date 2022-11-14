from dataclasses import dataclass, fields
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc


@dataclass
class TabNames:
    tab_1: str = 'tab_1'
    tab_2: str = 'tab_2'
    tab_3: str = 'tab_3'
    tab_4: str = 'tab_4'


@dataclass
class IDs:
    bar_chart_with_varying_bin_size = 'bar_chart_with_varying_bin_size'
    bar_chart_with_varying_bin_size_slider = 'bar_chart_with_varying_bin_size_slider'

    bar_chart_with_distributions = 'bar_chart_with_distributions'
    bar_chart_with_distributions_graph = 'bar_chart_with_distributions_graph'

    bar_chart_with_population_and_sample_data_slider = 'bar_chart_with_population_and_sample_data_slider'
    bar_chart_with_population_and_sample_data_dropdown = 'bar_chart_with_population_and_sample_data_dropdown'
    bar_chart_with_population_and_sample_data_distribution = 'bar_chart_with_population_and_sample_data_distribution'
    bar_chart_with_population_and_sample_data_sample_distribution = 'bar_chart_with_population_and_sample_data_sample_distribution'

    tab_output: str = 'tab_content'
    tab_input: str = 'tab_selector'


@dataclass
class Columns:
    @dataclass
    class NumericalVariables:
        id: int = 'ID'
        flight_distance: int = 'Flight Distance'
        departure_delay: int = 'Departure Delay'
        arrival_delay: int = 'Arrival Delay'
        age: int = 'Age'

    @dataclass
    class CategoricalVariables:
        gender: str = 'Gender'
        customer_type: str = 'Customer Type'
        type_of_travel: str = 'Type of Travel'
        class_: str = 'Class'
        departure_and_arrival_time_convenience: int = 'Departure and Arrival Time Convenience'
        ease_of_online_booking: int = 'Ease of Online Booking'
        check_in_service: int = 'Check-in Service'
        online_boarding: int = 'Online Boarding'
        gate_location: int = 'Gate Location'
        on_board_service: int = 'On-board Service'
        seat_comfort: int = 'Seat Comfort'
        leg_room_service: int = 'Leg Room Service'
        cleanliness: int = 'Cleanliness'
        food_and_drink: int = 'Food and Drink'
        in_flight_service: int = 'In-flight Service'
        in_flight_wifi_service = 'In-flight Wifi Service'
        in_flight_entertainment: int = 'In-flight Entertainment'
        baggage_handling: int = 'Baggage Handling'
        satisfaction: str = 'Satisfaction'


distributions = {

    'Uniform': 'st.uniform.rvs(size=1000, loc=10, scale=20)',
    'Normal': 'st.norm.rvs(size=1000, loc=0, scale=1)',
    'T distribution': 'st.t.rvs(size=1000, loc=0, scale=1, df=10)',
    'Gamma': 'st.gamma.rvs(a=2, size=1000)',
    'Exponential': 'st.expon.rvs(scale=1, loc=0, size=1000)',
    'Poisson': 'st.poisson.rvs(mu=3, size=1000)',
    'Binomial': 'st.binom.rvs(n=10, p=0.8, size=1000)',
    'Bernoulli': 'st.bernoulli.rvs(size=1000, p=0.6)',
    'Log-normal': 'st.lognorm.rvs(size=1000, loc=0, scale=1, s=22)',
    'Beta': 'st.beta.rvs(size=1000, a=5, b=1)',
    'Chi2': 'st.chi.rvs(70, size=1000)'

}


def create_histogram(
        df_: pd.DataFrame,
        numerical_column: str,
        number_of_bins: int = None,
        color_=None
):
    fig = px.histogram(
        data_frame=df_,
        color=color_,
        barmode='overlay',
        x=numerical_column,
        template='simple_white'
    )

    fig.update_traces(xbins=dict(
        size=number_of_bins
    ))

    return fig


def create_bar_chart(
        df_: pd.DataFrame,
        x_variable: str
):
    df_grouped = df_.groupby(x_variable, as_index=False).count()[[x_variable, 'ID']]
    # df_grouped = df_grouped.sort_values(by='ID')

    # Change x-axis variable to str so that we can plot it in specific order
    # Necessary when sorting DataFrame
    df_grouped = df_grouped.astype(dtype={x_variable: str})

    df_grouped.rename(columns={'ID': 'Number of passengers'}, inplace=True)

    fig = px.bar(df_grouped, x=x_variable, y="Number of passengers", template='simple_white')

    return fig


def create_scatter_plot(
        df_: pd.DataFrame,
        x: str,
        y: str
):
    fig = px.scatter(
        data_frame=df_.sample(n=1000),
        x=x,
        y=y,
        template='simple_white'
    )

    # https://plotly.com/python/marker-style/#opacity
    # https://chart-studio.plotly.com/~alex/455/four-ways-to-change-opacity-of-scatter-markers.embed
    fig.update_traces(marker=dict(
            # color='LightSkyBlue',
            # size=80,
            opacity=0.5,
            # line=dict(
            #     color='MediumPurple',
            #     width=8
            # )
        ), opacity=0.5)

    return fig


def create_simple_grid(
        input_list: list,
        number_of_columns_in_row: int
):
    return dmc.SimpleGrid(
        cols=number_of_columns_in_row,
        children=input_list
    )


