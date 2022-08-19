<?php
    class Student{
        private $name;

        // Getter
        public function getName(){
            return $this->name;
        }   

        // Setter
        public function setName($n){
            $this->name = $n;
        }        
    }
    
    $john = new Student();
    $john->setName("John");
    echo "".$john->getName();
?>