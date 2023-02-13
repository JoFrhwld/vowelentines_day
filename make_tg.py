from praatio import textgrid
import click


@click.command()
@click.argument("name", default = "Speaker")
@click.argument(
  "textpath", 
  type=click.Path(exists=True), 
  default = "passages/01_rainbow.txt"
  )
@click.argument(
  "duration"
  )
@click.argument(
  "outpath"
  )  
def makeTG(
  name,
  textpath,
  duration,
  outpath
):
  with open(textpath) as tp:
    text = tp.read()
    
  tg = textgrid.Textgrid()

  interval = textgrid.IntervalTier(
       name = name,
       entries = [(0, duration, text)],
       minT = 0,
       maxT = duration
       )

  tg.addTier(interval)

  tg.save(
    outpath, 
    format = "long_textgrid", 
    includeBlankSpaces = False
  )
  
if __name__ == "__main__":
  makeTG()
