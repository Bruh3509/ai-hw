package io.innowise.backend.config;

import io.innowise.backend.entity.AuthUser;
import io.innowise.backend.repository.AuthUserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
@Slf4j
public class DataInitializer implements ApplicationRunner {

    private final AuthUserRepository authUserRepository;
    private final PasswordEncoder passwordEncoder;

    @Override
    public void run(ApplicationArguments args) {
        if (authUserRepository.count() == 0) {
            log.info("Seeding initial authentication users...");

            AuthUser user1 = new AuthUser();
            user1.setName("Leanne Graham");
            user1.setEmail("Sincere@april.biz");
            user1.setPasswordHash(passwordEncoder.encode("password123"));
            authUserRepository.save(user1);

            AuthUser user2 = new AuthUser();
            user2.setName("Ervin Howell");
            user2.setEmail("Shanna@melissa.tv");
            user2.setPasswordHash(passwordEncoder.encode("password123"));
            authUserRepository.save(user2);

            log.info("Seeding complete.");
        }
    }
}
