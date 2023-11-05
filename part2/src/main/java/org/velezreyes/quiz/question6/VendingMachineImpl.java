package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
    private int balance;
    private static VendingMachineImpl instance;

    private VendingMachineImpl() {
        balance = 0;
    }

    public static VendingMachineImpl getInstance() {
        if (instance == null) {
            instance = new VendingMachineImpl();
        }
        return instance;
    }

    @Override
    public void insertQuarter() {
        balance += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        switch (name) {
            case "ScottCola":
                if (balance < 75) {
                    throw new NotEnoughMoneyException("Not enough money for ScottCola.");
                }
                balance -= 75;
                return new Drink("ScottCola", true);
            case "KarenTea":
                if (balance < 100) {
                    throw new NotEnoughMoneyException("Not enough money for KarenTea.");
                }
                balance -= 100;
                return new Drink("KarenTea", false);
            default:
                throw new UnknownDrinkException("Unknown drink: " + name);
        }
    }
}
