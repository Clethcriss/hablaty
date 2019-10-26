package com.junction.train;

import static org.springframework.web.bind.annotation.RequestMethod.GET;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class TrainApplication {
  Logger logger = LoggerFactory.getLogger(TrainApplication.class);


  @CrossOrigin
  @RequestMapping(value = "/", method = GET)
  public String index(){
    logger.info("route called");
    return "called the index route";
  }

  public static void main(String[] args) {
    SpringApplication.run(TrainApplication.class, args);
  }

}
