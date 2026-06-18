from dataclasses import dataclass
from datetime import datetime,timezone
from typing import Callable
@dataclass(frozen=True)
class Result:
 rule:str; passed:bool; failures:int; checked:int

def completeness(rows:list[dict],column:str,max_null_rate:float=0.0)->Result:
 failures=sum(r.get(column) in (None,"") for r in rows);checked=len(rows)
 return Result(f"completeness:{column}",(failures/checked if checked else 0)<=max_null_rate,failures,checked)
def uniqueness(rows:list[dict],column:str)->Result:
 values=[r.get(column) for r in rows];failures=len(values)-len(set(values))
 return Result(f"uniqueness:{column}",failures==0,failures,len(values))
def quarantine(rows:list[dict],predicate:Callable[[dict],bool]):
 passed,rejected=[],[]
 for row in rows:(passed if predicate(row) else rejected).append(row)
 return passed,rejected