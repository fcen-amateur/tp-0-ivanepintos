import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Americas"],
            x="year",
            y="lifeExp",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Expectativa de Vida en America",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="Expectativa de vida en países de Oceanía a lo largo del tiempo",
        autor="La cátedra",
        figura=figura,
    )

print (plot())