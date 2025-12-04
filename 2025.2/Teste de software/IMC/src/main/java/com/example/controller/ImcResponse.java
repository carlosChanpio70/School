package com.example.controller;

public class ImcResponse {
  private boolean success;
  private double imc;
  private String classification;
  private String error;

  public ImcResponse(boolean success, double imc, String classification,
                     String error) {
    this.success = success;
    this.imc = imc;
    this.classification = classification;
    this.error = error;
  }

  public boolean isSuccess() { return success; }

  public void setSuccess(boolean success) { this.success = success; }

  public double getImc() { return imc; }

  public void setImc(double imc) { this.imc = imc; }

  public String getClassification() { return classification; }

  public void setClassification(String classification) {
    this.classification = classification;
  }

  public String getError() { return error; }

  public void setError(String error) { this.error = error; }
}
