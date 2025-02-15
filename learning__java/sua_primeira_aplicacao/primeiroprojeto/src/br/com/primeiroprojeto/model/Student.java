package br.com.primeiroprojeto.model;

public class Student {
    private String name;
    private int age;
    private int registration;

    public Student(String name, int age, int registration) {
        this.name = name;
        this.age = age;
        this.registration = registration;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getRegistration() {
        return registration;
    }

    public void setRegistration(int registration) {
        this.registration = registration;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", registration=" + registration +
                '}';
    }
}
