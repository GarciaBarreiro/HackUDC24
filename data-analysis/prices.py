import pvpc
def get_electricity_cost(date):
    # Obtener valores para un día
    try:
        r = pvpc.get_pvpc_day(date)
        data = r.data.pcb.hours
        # "hours" es un diccionario, donde clave = horas del día, valores = coste en €/kWh
        electricity_cost = {}
        for hour, cost in data.items():
            electricity_cost.setdefault(hour, cost)
            #print(f"{hour}: {cost} €/kWh")
            # Ejemplo: "0h: 0.33694 €/kWh"
        #r.json()
    except pvpc.PVPCNoDataForDay:
        return {}
    return electricity_cost