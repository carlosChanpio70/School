# IMC Calculator - Enhanced with New Classes

## New Classes Integration

The web application has been successfully enhanced to utilize all 10 classes in your project:

### Classes Now in Use:

1. **Calculo** - Core IMC calculation engine
2. **Genero** - Gender-specific IMC ranges
3. **IMC** - Main IMC model class
4. **ImcApplication** - Spring Boot application entry point
5. **ImcController** - Enhanced REST controller with validation
6. **ImcResponse** - Response model for IMC calculations
7. **Pessoa** - User profile information storage
8. **ClassificacaoIMC** - IMC classification ranges (NEW)
9. **HistoricoCalculos** - Calculation history tracking (NEW)
10. **ValidadorDados** - Comprehensive data validation (NEW)

Plus 2 additional response classes:

-   **ValidationResponse** - Validation result responses
-   **ClassificacaoResponse** - Classification guide responses

## New Web Features

### 1. **Calculadora Tab** (Original Enhanced)

-   Enhanced validation using `ValidadorDados` class
-   Calculation history automatically tracked
-   Responsive UI with loading spinner

### 2. **Perfil Tab** (Uses `Pessoa` Class)

-   Create and edit user profile with name, age, gender
-   Profile persistence using browser localStorage
-   Integrated with IMC calculations

### 3. **Histórico Tab** (Uses `HistoricoCalculos` Class)

-   View complete history of all IMC calculations
-   Timestamps for each calculation
-   Statistics showing:
    -   Total number of calculations
    -   Average IMC value
-   Clear history option

### 4. **Classificações Tab** (Uses `ClassificacaoIMC` Class)

-   Reference guide showing IMC ranges for males and females
-   Color-coded classifications:
    -   Blue: Underweight
    -   Green: Normal weight
    -   Orange: Overweight
    -   Red: Obese

## New Backend Endpoints

### POST `/calcular`

-   Enhanced with `ValidadorDados` for comprehensive input validation
-   Returns calculation result with classification

### POST `/validar-pessoa`

-   Uses `ValidadorDados` to validate complete person data (name, age, gender, weight, height)
-   Creates `Pessoa` objects when validation passes

### GET `/classificacoes`

-   Returns `ClassificacaoIMC` objects for both genders
-   Provides complete IMC range reference

## Data Persistence

-   **Profile data**: Stored in browser localStorage
-   **Calculation history**: Persisted locally with timestamps
-   **Data survives browser restarts**

## Technical Improvements

1. **Comprehensive Input Validation**: All inputs validated using `ValidadorDados`
2. **Object-Oriented Design**: Leverages all 10 classes appropriately
3. **Tab-Based Navigation**: Clean, organized user interface
4. **Calculation Tracking**: Automatic history recording
5. **Statistics**: Aggregate calculations show average IMC
