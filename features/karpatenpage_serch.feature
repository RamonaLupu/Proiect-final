Feature: Test the karpaten page

  Background:
    Given Home page: I open karpaten home_page

  @Test1
  Scenario: Check the login_page - non-existent user
    When Home page: I go to login_page by click Contul meu
    When Login page: I send an invalid e-mail and password
    When Login page: I click on the button: Intra in cont
    Then Login page: I verify if the error is "Date de autentificare invalide."

  @Test2
    Scenario: Try to connect with google account- invalid e-mail
     When Home page: I click Contul meu
     When Login page: I click the button: Autentifica-te cu Google
     When Facebook page: I send an invalid e-mail
     When Facebook page: I click the button: Inainte
     Then Facebook page: I verify that the error is "Contul Google nu a fost găsit"

  @Test3
    Scenario: Try to connect with google account- valid e-mail
    When Home page: I navigate to login_page
    When Login page: I click on the button: Autentifica-te cu Google
    When Google page: I send my mail
    When Google page: I click Inainte
    Then Google page: I verify that the button: Incearca din nou is displayed

  @Test4
    Scenario: Check the register_page - textbox for Nume empty
    When Home page: I navigate to login_page by click Contul meu
    When Login page: I click on the button: Creeaza cont
    When Register page: I leave the textbox for Nume empty
    When Register page: I send Prenume
    When Register page: I send Email
    When Register page: I send a password on the textbox Parola
    When Register page: I resend the password on the textBox Verificare parola
    When Register page: I click on the button: Creeaza cont
    Then Register page: I verify if the error is "Va rog introduceti numele dvs."

  @Test5
  Scenario: Check the register_page - successful register
    When Home page: I go to login_page
    When Login page: I click on Creeaza cont
    When Register page: I send a Nume
    When Register page: I send an Prenume
    When Register page: I send an adress mail
    When Register page: I send  password on the textbox Parola
    When Register page: I resend the same password on the textBox Verificare parola
    When Register page: I click on the button: Creeaza cont
    Then Register page: I verify if the message for successful register is displayed

  @Test6
  Scenario Outline: Check the holiday offers from the home_page
    When Home page: I click on the Avion radio button
    When Home page: I search for destinatie
    When Home page: I search "<oras_plecare>"
    When Home page: I choose the date
    When Home page: I click on the button: Cauta
    Then Home page: I have at least 5 results returned

    Examples:
      | oras_plecare |
      | Cluj Napoca  |
      | Bucuresti    |

  @Test7
  Scenario: Check if the logo is displayed on the Despre-noi_page
    When Home page: I go to Despre-noi_page by click Despre noi
    Then Despre-noi page: I verify if the logo is displayed

  @Test8
  Scenario: Check if when I'm on the Last Minute page and I click on the logo it goes to the home_page
    When Home page: I go to LastMinute_page
    When LastMinute page: I click on the Logo
    Then Home page: I verify the url home_page

  @Test9
    Scenario: Check the button: Inapoi la site from the Karpaten_blog
    When Home page: I click on Blog
    When Blog Page: I click on button: Inapoi la site
    Then Home page: I verify if the currect url is "https://www.karpaten.ro/home/"

  @Test10
  Scenario: Check the price for a holiday at the Kleopatra Royal Hotel
    When Home page: In the textbox of Cauta destinatie,hotel I write "Kleopatra Royal Palm Hotel Alanya"
    When Oferta Cazare page: I check if the avion button is selected
    Then Oferta Cazare page: I verify if the starting price is less than 600€

  @Test11
  Scenario: Check the tourist evaluation for a holiday at the Kleopatra Royal Hotel
    When Home page: I search "Kleopatra Royal" from the Cauta destinatie, hotel
    Then Oferta Cazare page: I verify if the tourist evaluation is "Foarte bine"


