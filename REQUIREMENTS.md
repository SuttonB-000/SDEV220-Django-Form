# Django Student Registration — Requirements

## Overview

Create a Django project and application that provides a student registration form. The application must collect student information, validate required fields, and display the submitted information on a confirmation/results page.

---

# Part 1 — Django Project and Application

## R1 — Django Project

Create a new Django project.

**Acceptance criteria:**

* A valid Django project exists.
* The project can be started successfully using Django's development server.
* The project configuration is valid.

## R2 — Django Application

Create at least one Django application within the project.

**Acceptance criteria:**

* At least one Django application exists.
* The application is properly registered/configured in the Django project.

## R3 — URL Routing

The project must include URL routing.

**Acceptance criteria:**

* The Django project has URL configuration.
* The application has appropriate URL routing.
* At least one URL maps to the form page/view.

## R4 — Views

The application must contain at least one Django view.

**Acceptance criteria:**

* At least one view handles an HTTP request.
* The view renders the appropriate HTML template.

## R5 — HTML Templates

The project must contain at least two HTML templates.

**Acceptance criteria:**

* At least two distinct HTML template files exist.
* One template is used for the student registration form.
* One template is used for displaying the results/confirmation page.

---

# Part 2 — Create an HTML Form

## R6 — Student Registration Form

Create an HTML form containing all of the required fields and widgets below.

| Field                       | Required Widget      |
| --------------------------- | -------------------- |
| Student Name                | Text Box             |
| Student ID                  | Text Box             |
| Major                       | Drop-down List       |
| Class Standing              | Radio Buttons        |
| Programming Languages Known | Checkboxes           |
| Expected Graduation Year    | Number Input         |
| Comments                    | Multi-line Text Area |
| Submit                      | Button               |

## R7 — Student Name

The form must contain a **Student Name** text box.

**Acceptance criteria:**

* A text input exists for Student Name.
* The submitted value can be retrieved by the application.

## R8 — Student ID

The form must contain a **Student ID** text box.

**Acceptance criteria:**

* A text input exists for Student ID.
* The submitted value can be retrieved by the application.

## R9 — Major

The form must contain a **Major** drop-down list.

**Acceptance criteria:**

* A select/drop-down widget exists for Major.
* The user can select a major.
* The selected value can be retrieved by the application.

## R10 — Class Standing

The form must contain **Class Standing** radio buttons.

**Acceptance criteria:**

* Radio buttons are provided for Class Standing.
* The user can select a class standing.
* The selected value can be retrieved by the application.

## R11 — Programming Languages Known

The form must contain **Programming Languages Known** checkboxes.

**Acceptance criteria:**

* Multiple checkbox options are provided.
* The user can select zero or more programming languages.
* All selected values can be retrieved by the application.

## R12 — Expected Graduation Year

The form must contain an **Expected Graduation Year** number input.

**Acceptance criteria:**

* An HTML number input is used.
* The submitted value can be retrieved by the application.

## R13 — Comments

The form must contain a **Comments** multi-line text area.

**Acceptance criteria:**

* A multi-line textarea is provided.
* The submitted value can be retrieved by the application.

## R14 — Submit Button

The form must contain a **Submit** button.

**Acceptance criteria:**

* The button submits the form.
* Submitting the form sends the form data to the Django application for processing.

---

# Part 3 — Process the Form

## R15 — Form Submission

When the user clicks **Submit**, the Django application must process the submitted form.

**Acceptance criteria:**

* The application receives the submitted form data.
* The application distinguishes between valid and invalid submissions.

## R16 — Validate Student Name

The application must validate that **Student Name is not blank**.

**Acceptance criteria:**

* An empty Student Name is considered invalid.
* A non-empty Student Name passes this validation.

## R17 — Validate Student ID

The application must validate that **Student ID is not blank**.

**Acceptance criteria:**

* An empty Student ID is considered invalid.
* A non-empty Student ID passes this validation.

## R18 — Display Validation Errors

If validation fails, the application must display an error message.

**Acceptance criteria:**

* A submission with a blank Student Name displays an error.
* A submission with a blank Student ID displays an error.
* The user can see which required information needs to be corrected.
* The form remains available so the user can correct the submission.

## R19 — Process Valid Submission

If validation succeeds, the application must collect the submitted values.

**Acceptance criteria:**

* Student Name is collected.
* Student ID is collected.
* Major is collected.
* Class Standing is collected.
* Programming Languages Known is collected.
* Expected Graduation Year is collected.
* Comments is collected.

## R20 — Pass Data to Results Page

After successful validation, the application must pass the submitted values to a results/confirmation page.

**Acceptance criteria:**

* A successful submission navigates to the results/confirmation page.
* The submitted values are available to the results page.
* The results page displays the submitted information rather than hard-coded values.

---

# Part 4 — Display Results

## R21 — Confirmation Page

Create a confirmation/results page displayed after a successful form submission.

**Acceptance criteria:**

* The page is displayed only after a valid submission.
* The page clearly identifies the submission as a student registration.
* The page displays the student's submitted information.

## R22 — Student Registration Summary

The confirmation page must contain a **Student Registration Summary** with the following information:

* Student Name
* Student ID
* Major
* Class Standing
* Programming Languages
* Expected Graduation

**Acceptance criteria:**

* Student Name is displayed.
* Student ID is displayed.
* Major is displayed.
* Class Standing is displayed.
* All selected Programming Languages are displayed.
* Expected Graduation Year is displayed.

---

# Minimum Deliverables

The completed project must contain, at minimum:

* A working Django project.
* At least one Django application.
* URL routing.
* At least one Django view.
* At least two HTML templates.
* A student registration HTML form.
* All required form widgets.
* Validation for Student Name.
* Validation for Student ID.
* Error messages for failed validation.
* Processing of valid submissions.
* A results/confirmation page.
* A Student Registration Summary displaying the required submitted information.

# Functional Flow

The expected application flow is:

1. User navigates to the student registration page.
2. User completes the registration form.
3. User clicks **Submit**.
4. Django validates Student Name.
5. Django validates Student ID.
6. If either required field is blank:

   * Display an error message.
   * Keep the user on the form page.
7. If validation succeeds:

   * Collect all submitted values.
   * Pass the values to the results page.
8. Display the **Student Registration Summary**.
9. The summary displays:

   * Student Name
   * Student ID
   * Major
   * Class Standing
   * Programming Languages
   * Expected Graduation

