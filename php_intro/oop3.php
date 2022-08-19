<?php
    class Book{
        public $title, $isbn, $copies;

        function __construct($title, $isbn, $copies){
            $this->title = $title;
            $this->isbn = $isbn;
            $this->copies = $copies;
        }
    }
    $book = new Book($title="The Great Gasby",$isbn="202211221",$copies=1999238);
    echo $book->title;
?>