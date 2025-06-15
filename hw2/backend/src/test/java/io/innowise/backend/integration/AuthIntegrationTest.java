package io.innowise.backend.integration;

import io.innowise.backend.dto.LoginRequestDto;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;

import static org.springframework.security.test.web.servlet.request.SecurityMockMvcRequestPostProcessors.csrf;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Integration tests specifically for the authentication controller.
 */
public class AuthIntegrationTest extends AbstractIntegrationTest {

    @Test
    void whenLoginWithValidCredentials_shouldReturnJwtToken() throws Exception {
        LoginRequestDto loginRequest = new LoginRequestDto("Sincere@april.biz", "password123");

        mockMvc.perform(post("/auth/login")
                        .with(csrf()) // Use csrf() for POST requests in tests
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(loginRequest)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.token").exists())
                .andExpect(jsonPath("$.token").isString());
    }

    @Test
    void whenLoginWithInvalidPassword_shouldReturnUnauthorized() throws Exception {
        LoginRequestDto loginRequest = new LoginRequestDto("Sincere@april.biz", "wrongpassword");

        mockMvc.perform(post("/auth/login")
                        .with(csrf())
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(loginRequest)))
                .andExpect(status().isForbidden());
    }

    @Test
    void whenLoginWithNonExistentUser_shouldReturnUnauthorized() throws Exception {
        LoginRequestDto loginRequest = new LoginRequestDto("notauser@example.com", "password123");

        mockMvc.perform(post("/auth/login")
                        .with(csrf())
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(loginRequest)))
                .andExpect(status().isForbidden());
    }
}
