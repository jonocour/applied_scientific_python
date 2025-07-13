import click

@click.command()
@click.option("--mass", type=float, required=True, help="Mass in kg")
@click.option("--acceleration", type=float, required=True, help="Acceleration in m/s²")
def cli(mass, acceleration):
    """Compute force using Newton's 2nd Law: F = m * a"""
    force = mass * acceleration
    click.echo(f"Force = {force:.2f} N")


