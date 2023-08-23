import BSV as bsv


manager = bsv.gateManager()

manager.addGate(bsv.GATEBOX())
manager.addGate(bsv.GATEBOX(bsv.GATE_BOX , 1 , 1 , [1,0]))
manager.addGate(bsv.GATEBOX(bsv.TERMINAL_OUT,1))


manager.connectGatesToInput(1 , 2 , 0)
manager.connectGatesToInput(2 , 3 , 0)

manager.resetTerminalGate(1)

manager.simulate()
print(manager.getFinalGateVectors())
print(manager.getFinalGateOutputs())


