<?php
    class Student{
        var $name;
        function __set($propName, $propValue){
            echo "Nonexistent variable \$$propName";
        }
    }
    
    $john = new Student();
    $john->title = "John";
?>