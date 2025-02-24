from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, '[aria-label="Ir a la página principal de kayak"]')
    signin_button = (By.CSS_SELECTOR, 'button[aria-label="Buscar"]')
    menu_button = (By.CSS_SELECTOR, 'div[aria-label="Abrir navegación principal" ]')
    search_for_flights = (By.CSS_SELECTOR, '[aria-label="Buscar vuelos "]')
    search_for_hotels = (By.CSS_SELECTOR, '[aria-label="Buscar hoteles "]')
    car_search = (By.CSS_SELECTOR, '[aria-label="Buscar autos "]')
    Go_to_Explore = (By.CSS_SELECTOR, '[aria-label="Ir a Explore "]')
    Visit_our_blog = (By.CSS_SELECTOR, '[aria-label="Visita nuestro blog "]')
    Search_for_direct_flights = (By.CSS_SELECTOR, '[aria-label="Buscar vuelos directos "]')
    best_time_to_travel= (By.CSS_SELECTOR, '[aria-label="Descubre el mejor momento para viajar "]')
    KAYAK_for_Business = (By.CSS_SELECTOR, '[aria-label="KAYAK for Business NUEVO"]')
    Trips = (By.CSS_SELECTOR, '[aria-label="Trips "]')
    Spanish = (By.CSS_SELECTOR, '[aria-label="Español"]')
    Colombian_peso = (By.CSS_SELECTOR, '[aria-label="Peso colombiano "]')
    