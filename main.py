from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

""""
createroute SYD MEL
createroute SYD MEL
findroute 1
findroute 2
removeroute 1
removeroute 2
createpackage SYD MEL 40 IV
createpackage SYD MEL 15 IV
createpackage SYD MEL 15 IV
findpackage 1
findpackage 2
findpackage 3
removepackage 1
removepackage 2
removepackage 3
findpackage 1
findpackage 2
findpackage 3
viewpackage
viewroute
end

createroute SYD MEL
createpackage SYD MEL 10 iv 
findroute 1 
findpackage 1
removeroute 1 
removepackage 1 
findroute 1 
findpackage 1 
createroute MEL ASP 
createpackage MEL ASP 40 WI 
findroute 2 
findpackage 2 
viewroute 
viewpackage 
end

createroute SYD MEL ASP PER
createroute SYD MEL
createpackage SYD MEL 10500 DAN
createpackage MEL ASP 10500 IVO
createpackage ASP PER 10500 ZDR
createpackage SYD PER 10500 AS
createpackage SYD MEL 55 IVAN
viewpackage
viewroute
end

createroute SYD MEL ADL
createroute SYD MEL
createpackage SYD MEL 15000 DAN
createpackage SYD MEL 15000 IVO
createpackage SYD MEL 13000 ZDR
createpackage SYD MEL 5000 AS
viewpackage
viewroute
end

createroute SYD MEL ADL
createroute SYD MEL
createroute MEL ASP BRI
createroute DAR PER
createroute ADL BRI MEL
createpackage SYD MEL 15000 DAN
createpackage SYD MEL 15000 IVO
createpackage SYD MEL 13000 ZDR
createpackage SYD MEL 5000 AS
createpackage MEL ASP 20000 MAX
createpackage MEL ASP 15000 LUC
createpackage DAR PER 30000 ANN
viewpackage
viewroute
findroute 1
findroute 3
findpackage 1
findpackage 5
removeroute 2
removepackage 3
removepackage 7
viewpackage
viewroute
end

createroute SYD MEL ADL 
createroute SYD MEL 
createpackage SYD MEL 15000 DAN 
createpackage SYD MEL 15000 IVO 
createpackage SYD MEL 13000 ZDR 
createpackage SYD MEL 5000 AS 
removepackage 1 
createpackage MEL ADL 15000 DAN 
viewpackage 
viewroute 
end

createroute SYD MEL ADL 
createroute SYD MEL 
createpackage SYD MEL 15000 DAN 
createpackage SYD MEL 15000 IVO 
createpackage SYD MEL 13000 ZDR 
createpackage SYD MEL 5000 AS 
removepackage 1 
createroute MEL ADL
createpackage MEL ADL 15000 DAN 
viewpackage 
viewroute 
end
"""