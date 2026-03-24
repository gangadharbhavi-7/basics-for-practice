package java_programming;

class Animal {
    private String name = "elephant";

    void sound() {
        System.out.println(name + " makes trumpet sound");
    }
}

class Dog extends Animal {
    private String name = "bow";

    @Override
    void sound() {
        super.sound();
        System.out.println(name + " makes bow bow");
    }

    String getName() {
        return name;
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        System.out.println(d.getName());
        d.sound();
    }
}