package com.cloudcomputing.test.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoController {

    @GetMapping(value = "/hello")
    public String Hello() {
        return "Pozdrav!";
    }
}
