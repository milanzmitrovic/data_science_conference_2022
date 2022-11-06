from dataclasses import dataclass, fields
import pandas as pd
import plotly.express as px


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
    'T distribution': 'st.t.rvs(size=1000, loc=0, scale=1, df=99)',
    'Gamma': 'st.gamma.rvs(a=5, size=1000)',
    'Exponential': 'st.expon.rvs(scale=1, loc=0, size=1000)',
    'Poisson': 'st.poisson.rvs(mu=3, size=1000)',
    'Binomial': 'st.binom.rvs(n=10, p=0.8, size=1000)',
    'Bernoulli': 'st.bernoulli.rvs(size=1000, p=0.6)',
    'Log-normal': 'st.lognorm.rvs(size=1000, loc=0, scale=1, s=22)',
    'Beta': 'st.beta.rvs(size=1000, a=33, b=33)'

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


def create_bar_chart():

    return ''


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

    return fig





